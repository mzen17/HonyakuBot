# Terminal System

from comparison import Comparator
from sentmanager import SentManager
import os

print("Welcome to HonyakuBot.")
print("Let the fun begin! :D")

while True:
    print("Waiting for command... [Type 'h' for help]")
    dirname = os.path.dirname(__file__)
    sentmanager = SentManager(f"{dirname}/sampledata/jp-eng.tsv")

    command = input("> ")
    if ( command == "q"):
        break;
    elif ( command == "h"):
        print("Commands:")
        print("q - quit")
        print("h - help")
        print("n - new sentence")
    elif ( command == "n"):
        
        test = sentmanager.get_random_sentence()

        print("Translate: [" + test[0] + "]")

        translation = input("> ")

        comparator = Comparator()
        score = comparator.compare_sentences(test[1], translation)

        print("Score: " + str(score))
        print("Correct answer: [" + test[1] + "]")
    

