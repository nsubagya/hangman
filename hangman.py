#from replit import clear
#import os
from IPython.display import clear_output
import random as rand
from hangman_arts import logo,stages
from hangman_words import english_word_list
#word_list = ["Cat", "Apple", "Walmart"]# change this to a bigger word list by importing later
# Clear the console screen
random_word=rand.choice(english_word_list).lower()
random_word_length = len(random_word)
print(logo)
print(random_word)#clear this
print('Word length is: ',random_word_length)# may be keep this
lives=6
win_game = False
#display = []
#for _ in range(random_word_length):
#    display +='_'
display = ['_'] * len(random_word)
print(f"{' '.join(display)}")
print('you have 6 lives')
non_correct_letters = []




while (lives != 0) and (win_game == False):#or not win_game(ctrl+] indent)

        guess = input("Guess a letter: ").lower()
        
        #os.system('cls')#this is to clear previous
        #os.system('cls' if os.name == 'nt' else 'clear')#clear console
        if guess in display:
            print(f'\nyou already gussed the letter {guess}, guess another one')

        if guess in non_correct_letters:
            print(f'\nyou already gussed the letter {guess} which is not correct, guess another one')

        elif guess in random_word:
            for index, letter in enumerate(random_word):
                if letter == guess:
                    display[index]=letter
                    if '_' not in display:
                        print('\nCongratulations you won!')
                        win_game = True
        elif guess not in random_word:
            clear_output(wait=True)
            print(f'\nThe guess {guess} was wrong, try again!')
            non_correct_letters.append(guess)
            lives -= 1
            print(stages[lives])
            if lives == 0:
                print('\nSorry, you lost a life.')
                print('Word to be gussed was: ', random_word)

        # Print the updated display, lives, and win_game status
        #print(' '.join(display))
        print(f'\nLives remaining: {lives}')
        print(f'Win status: {"yes" if win_game else "no"}')
        print("Incorrect guesses:", non_correct_letters)
        print('Word gussed upto now is: ',f"{' '.join(display)}")
        #print(lives)
        #print(win_game)
