# Terminal System

print("Loading...")

from comparison import Comparator
from sentmanager import SentManager
import os

dirname = os.path.dirname(__file__)
sentmanager = SentManager(f"{dirname}/sampledata/jp-eng.tsv")
comparator = Comparator()


print("Welcome to HonyakuBot.")
print("Let the fun begin! :D")
reverse = False

while True:
    print("Waiting for command... [Type 'h' for help]")

    command = input("> ")
    if ( command == "q"):
        break;
    elif ( command == "r"):
        reverse = not reverse
        print("Reverse mode: " + str(reverse))   
    elif ( command == "h"):
        print("Commands:")
        print("q - quit")
        print("h - help")
        print("r - reverse")
        print("n - new sentence")
    elif ( command == "n"):
        
        test = sentmanager.get_random_sentence()

        if (reverse):
            test = ( test[1], test[0])

        print("Translate: [" + test[0] + "]")

        translation = input("> ")
        score = comparator.compare_sentences(test[1], translation)

        print("Score: " + str(score))
        print("Correct answer: [" + test[1] + "]")
    

