# FastAPI Libs
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# System Libs
import secrets
import hashlib
import os

# Internal Libs
from app.comparison import Comparator
from app.sentmanager import SentManager
from app.reader import Reader

dirname = os.path.dirname(__file__)
sentmanager = SentManager(f"data/jp-eng.tsv")
comparator = Comparator()
r = Reader("static")


app = FastAPI()
# Base URI in case running in an environment that attaches a base uri.
if "BASE_URI" in os.environ:
    BASE_URI = os.environ["BASE_URI"]
else:
    BASE_URI = ""

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Session KV.
# In memory store to prevent project from needing excessive services (such as a redis)
session_KV = {}


# Return HTML
templates = Jinja2Templates(directory="templates")
@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html",{"request": request, "URI":BASE_URI})


# Session Creation:
# Generates random string of tokens for session management
import time
@app.get("/new")
async def create_session():
    random_bytes = secrets.token_bytes(16)
    hash_object = hashlib.sha256(random_bytes)
    hashed_bytes = hash_object.digest()
    random_string = hashed_bytes.hex()[:16]

    session_KV[random_string] = {"phase":0, "reverse":False,"expire":time.time()+3600, "listen":False} 
    return {"KEY":random_string}

class KEY_TO_VAL(BaseModel):
    KEY: str

# Validating Session API
# Ensures that key is valid and not expired.
@app.post("/validate")
async def validate_session(recieve: KEY_TO_VAL):
    status = False
    if recieve.KEY in session_KV and time.time() < session_KV[recieve.KEY]["expire"]:
        status = True
    return {"KEY":status}


# Terminal Input
class SUBMISSION(BaseModel):
    KEY: str
    command: str

@app.post("/submission")
async def update_session(sub: SUBMISSION):
    output="Bad Command [If you type correct command, try purging session]"
    ef = ""

    # Make sure key is valid
    if sub.KEY in session_KV and time.time() < session_KV[sub.KEY]["expire"]:
        
        phase = session_KV[sub.KEY]['phase']

        # Phase 1 means it has sent sentence
        if(phase == 1):
            # Retrieve test and compare
            test = session_KV[sub.KEY]['problem']
            score = comparator.compare_sentences(test[1], sub.command)

            # Return output
            p_statement = f"Problem: [{test[0]}]\n\nYour Answer: {sub.command}\nCorrect answer: [{test[1]}]"
            output = f"{p_statement}\nScore: {str(score)}"
            session_KV[sub.KEY]['phase'] = 0

        # Generate new
        if(phase == 0 and sub.command == 'n'):
            # Set phase to mean it has sent sentence
            session_KV[sub.KEY]['phase'] = 1
            test = sentmanager.get_random_sentence()

            # Reverse mode reverses sentence (ex: en->jp, now jp->en)
            if ( session_KV[sub.KEY]['reverse']):
                test = (test[1], test[0])

            # Build output
            session_KV[sub.KEY]['problem'] = test
            output = "Translate:\n\n["+ test[0] + "]"

            # If listen mode, attach the listen media
            if(session_KV[sub.KEY]["listen"]):
                ef = r.produce_sound(test[0])
                output = "Listen to the attached audio."

        # Toggle reverse or listening
        if(phase == 0 and sub.command == 'r'):
            session_KV[sub.KEY]['reverse'] = not session_KV[sub.KEY]['reverse']
            output = "Reverse mode: " + str(session_KV[sub.KEY]['reverse'])

        if(phase == 0 and sub.command == 'l'):
            session_KV[sub.KEY]['listen'] = not session_KV[sub.KEY]['listen']
            output = "Listen mode: " + str(session_KV[sub.KEY]['listen'])

        # Return help
        if(phase == 0 and sub.command == 'h'):
            output = "Commands:\nh - help\nr - reverse\nl - enable or disable listen\nn - new sentence"

    return {"output":output, "file":ef}