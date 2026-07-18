<<<<<<< HEAD
import random

words = ('mayank', 'shilpa', 'ravi', 'mango', 'watermelon')

hangman_art = {0: ("  ",
                   "  ",
                   "  "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " ! ",
                   "   "),
               3: (" O ",
                   "/! ",
                   "   "),
               4: (" O ",
                   "/!\\",
                   "   "),
               5: (" O ",
                   "/!\\",
                   "/  "),
               6: (" O ",
                   "/!\\",
                   "/ \\")
               }
guessing = random.choice(words)
dashes = []
for letters in range(len(guessing)):
    dashes.append(" _ ")
guessing = list(guessing)
is_running = True
wg = 0
guessed_letters = set()
while is_running:
    print("*****************************")
    if wg < 6:
        for line in hangman_art[wg]:
            print(line)
    elif wg == 6:
        for line in hangman_art[wg]:
            print(line)
        print("----------------------")
        print("You Lose!")
        print("The word was: ")
        for letter in guessing:
            print(letter, end = "")
        print()
        print("----------------------")
        is_running = False
        break
    print("******************************")
    for dash in dashes:
        print(dash, end = "\t")
    print()
    guess = input("Enter your guess of one letter: ").lower()  
    if len(guess) > 1 or not guess.isalpha():
        print("Invalid Guess.")
        continue
    elif guess in guessed_letters:
        print("Letter already guessed.\nTry again.")
        continue
    else:
        if guess in guessing:
            for i in range(len(guessing)):
                if guessing[i] == guess:
                    dashes[i] = guess
        else:
            wg += 1  
    guessed_letters.add(guess)
    if dashes == guessing:
        for dash in dashes:
            print(dash, end = "\t")
        print()
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        print("You Win!")
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        is_running = False

            
                
            
                
                
                
    
        
=======
import random

words = ('apple', 'pineapple', 'mango', 'watermelon', 'grapes')

hangman_art = {0: ("  ",
                   "  ",
                   "  "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " ! ",
                   "   "),
               3: (" O ",
                   "/! ",
                   "   "),
               4: (" O ",
                   "/!\\",
                   "   "),
               5: (" O ",
                   "/!\\",
                   "/  "),
               6: (" O ",
                   "/!\\",
                   "/ \\")
               }
def win():
    if dashes == guessing:
        for dash in dashes:
            print(dash, end = "\t")
        print()
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        print("You Win!")
        print("⭐⭐⭐⭐⭐⭐⭐⭐⭐")
        is_running = False
guessing = random.choice(words)
dashes = []
for letters in range(len(guessing)):
    dashes.append(" _ ")
guessing = list(guessing)
is_running = True
wg = 0
guessed_letters = set()
while is_running:
    print("*****************************")
    if wg < 6:
        for line in hangman_art[wg]:
            print(line)
    elif wg == 6:
        for line in hangman_art[wg]:
            print(line)
        print("----------------------")
        print("You Lose!")
        print("The word was: ")
        for letter in guessing:
            print(letter, end = "")
        print()
        print("----------------------")
        is_running = False
        break
    print("******************************")
    for dash in dashes:
        print(dash, end = "\t")
    print()
    guess = input("Enter your guess of one letter: ").lower()
    if guess == guessing:
        win()
        break  
    elif len(guess) > 1 or not guess.isalpha():
        print("Invalid Guess.")
        continue
    elif guess in guessed_letters:
        print("Letter already guessed.\nTry again.")
        continue
    else:
        if guess in guessing:
            for i in range(len(guessing)):
                if guessing[i] == guess:
                    dashes[i] = guess
        else:
            wg += 1  
    guessed_letters.add(guess)
    win()

            
                
            
                
                
                
    
        
>>>>>>> c8e060a (second commit)
