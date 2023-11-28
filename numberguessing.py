from random import randint

ans = randint(0,100)
guess = input("Guess the number between 0 and 100 inclusive! I will tell you if you are hot or cold.  Good Luck!\n")
guess = int(guess)


while (ans != guess):
    if (int(guess) == ans):
        print("You win! The answer was ", ans, " :) \n")
        break
    elif (abs(ans-int(guess)) > 10):
        guess = input("You're a little cold :( guess again!\n")
    elif (3 < abs(ans-int(guess)) <= 10):
        guess = input("You're warm, guess again!\n")
    elif (abs(ans-int(guess)) <= 3):
        guess = input("You're burning!\n")
else:
    print("You win! The answer was ", ans, " :)\n")