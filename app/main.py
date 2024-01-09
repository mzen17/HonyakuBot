# Terminal System

from comparison import Comparator

print("Welcome to HonyakuBot.")
print("Let the fun begin! :D")

while True:
    print("Waiting for command... [Type 'h' for help]")

    command = input("> ")
    if ( command == "q"):
        break;
    elif ( command == "n"):
        print("Translate bob:")

        translation = input("> ")

        comparator = Comparator()
        score = comparator.compare_sentences("the snow fell early", translation)

        print("Score: " + str(score))
    

