"""
==============================================
                  Hangman v1.0
                By Lachlan Evans
==============================================
This was made for my Year 12 Information Technology project feel free to use it however you please.
    Libraries
"""
import os
import pickle
import random

"""
    Word Lists
    G-Words was a bit of boredom in class feel free to add it to difficulty selection
"""
hwords = ["gypsy", "onomatopeia", "bungler", "banjo", "crypt", "dwarves"]
# Do not judge me for I was bored in class. V
gwords = ["crips", "bloods", "yeet", "hood", "glock", "g"]

mwords = ["medium", "coight", "michael", "velocity", "funny"]

ewords = ["dog", "cat", "hello", "goodbye", "world"]


guesses = ''
trys = 10
amount = 0

random.shuffle(hwords)

random.shuffle(gwords)

random.shuffle(mwords)

random.shuffle(ewords)
"""
    Saving and loading data using pickle
"""
# Function using pickle to load existing files for scores
def load_data(file_name):
    print('loading %s file' % file_name)
    file_handle = open(file_name + ".p", "rb")
    data = pickle.load(file_handle)
    file_handle.close()
    return data

# If no file exists for scores this function creates one and saves winning score
def save_data(file_name, data):
    print('saving score in %s file' % file_name)
    file_handle = open(file_name + '.p', 'wb')
    pickle.dump(data, file_handle)
    file_handle.close()

# Python requires global variables if a variable is being used in a loop
global difficulty

difficulty_input = (input('Enter difficulty(easy, medium, hard): '))

difficulty_selected = False

"""
    Difficulty Selection
"""
# Probably a bad way to create a difficulty selection function but that is what it does.
while not difficulty_selected:
    if difficulty_input == 'easy':
        difficulty = 'easy'
        rand_word = random.choice(ewords)
        difficulty_selected = True
        break

    elif difficulty_input == 'medium':
        difficulty = 'medium'
        rand_word = random.choice(mwords)
        difficulty_selected = True
        break

    elif difficulty_input == 'hard':
        difficulty = 'hard'
        rand_word = random.choice(hwords)
        difficulty_selected = True
        break
    else:
        difficulty_input = (input('Please enter valid difficulty (easy, medium or hard): '))

scores = []


if os.path.exists(difficulty + ".p"):
    scores = load_data(difficulty)

"""
    Main Game
"""
while trys > 0:

    failed = 0

    for char in rand_word:
        if char in guesses:
            print(char),
        else:
            print("_"),
            failed += 1
"""
    End of Game Win
"""
    if failed == 0:
        print("You won!")
        print("Wrong guesses made: " + str(amount))
        score = amount
        scores.append(score)
        save_data(difficulty, scores)
        print(scores)
        print("Average wrong guesses in %s mode: %s" % (difficulty, (sum(scores) / len(scores))))
        break

    guess = input("guess a character:")[0]
    guesses += guess

    if guess not in rand_word:
        trys -= 1
        amount += 1
        print("Wrong")
        print("You have", + trys, 'more guesses')
"""
    End of Game Loss
"""
        if trys == 0:
            print("You Lose")
            print("The word was", rand_word)

