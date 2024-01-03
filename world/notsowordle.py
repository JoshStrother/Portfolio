#importing libraries
import json
import random
import numpy as np
from colorama import Fore
#import getpass this isnt implemented yet, thoughts for later

#uses the json package to import my preset words as a dictionary
def load_words(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return(data)

#here is the main method for the game to start
def word_game():
    word_base: dict = load_words('/Users/josh/NotSoWordle/mywords.json')

    #this chooses a random word and splits it into the letters as lower case so it can be read easier
    choose = random.randint(0, len(word_base["words"]))
    choices = word_base["words"]
    answer = choices[choose]
    answer = answer.lower()
    letters = list(answer)

    #print(answer) <- CASE TEST PURPOSES
    
    #this takes the users intial input and makes sure that it is 5 letters only to which it will then pass it to the play method
    guess = list(input("Enter a 5 letter word: "))
    if (len(guess)==5):
        play(guess, letters, answer)
    else:
        while(len(guess) != 5):
            guess = list(input("5 letter words ONLY: "))
        play(guess, letters, answer)

#this method takes users guess and compares it to the answer while also applying
        #colors so the player knows if the letter is in the word or not
def play(guess, letters, answer):
    #this variable keeps track of the number of guess, so we can allow the player only 6 guesses
    count = 1
    if (np.array_equal(guess, letters) == True):
        print("That's correct:", answer)
    else:
        while (np.array_equal(guess, letters) == False and count < 6):
            if(len(guess) != 5):
                guess = list(input("Enter a 5 letter word: "))
            for ch in range(0, 5, 1):
                if (guess[ch] == letters[ch]):
                    print(Fore.GREEN + f"{guess[ch]}", end='')  

                elif (guess[ch] in letters):
                        print(Fore.YELLOW + f"{guess[ch]}", end='')

                else:
                    print(Fore.RED + f"{guess[ch]}", end='')
            print('\n')
            count += 1
            guess = list(input(Fore.WHITE + f"Enter guess #" + str(count) + " : "))
        if (np.array_equal(guess, letters) == True):
            print("That's correct! The answer is: ", Fore.GREEN + answer)
        else:
            print("You ran out of tries! The correct answer is: ", Fore.GREEN + answer)
        
        



word_game()

