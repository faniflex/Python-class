import random
while True:
    correctGuess = random.randint(1,10)
    attempt = 0
    while attempt<3:
        attempt=attempt+1
        
        userGuess = int(input("Make a guess 1-10: "))
        if userGuess==correctGuess:
            print("Correct!")
        else:
            print("Wrong")
            if userGuess<correctGuess:
                print("you guessed Lower")
            else:
                print("you guessed Higher")
        print(f"this is your {attempt} Attempt")