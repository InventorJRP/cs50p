
def getGuess():
    guess = input("Guess a number 1-10: ")
    return guess

def main():
    guess = getGuess()
    if guess == "5":
        print("Correct")
    else:
        print("wrong")

    
main()