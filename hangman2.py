import random

HANGMAN_PICS = ['''
 +---+
     |
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
 |   |
/    |
    ===''','''
 +---+
 O   |
/|\  |
 |   |
/ \  |
    ===''','''
 +---+
[O   |
/|\  |
 |   |
/ \  |
    ===''','''
 +---+
[O]  |
/|\  |
 |   |
/ \  |
    ===''']

words = {
'colors': 'maroon red orange yellow green blue indigo violet pink white black brown'.split(),
'shapes': 'square triangle rectangle circle ellipse rhombus lozange trapezoid chevron pentagon hexagon septagon octagon cylinder cube sphere ellipse prism'.split(),
'fruits': 'apple orange lemon lime pear watermelon grape grapefruit banana cantaloupe mango strawberry tomato pomegranate cherry mango papaya kiwi pineapple apricot peach plum lychee'.split(),
'animals': 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split(),
'vegetables': 'cucumber onion garlic carrot lettuce potato cabbage radish eggplant mushroom zucchini pepper artichoke corn beet broccoli avocado spinach cauliflower celery chili bean asparagus olive pumpkin turnip'.split(),
'gemstones': 'agate alexandrite amber amethyst apatite aquamarine bloodstone calcite carnelian citrine diamond emerald fluorite garnet jade jasper malachite moonstone obsidian onyx opal pearl peridot quartz ruby sapphire topaz tourmaline turquoise zircon'.split(),
'plants': 'tulip daffodil poppy sunflower dandelion hyacinth daisy rose crocus orchid iris peony chrysanthemum geranium lily lotus peony carnation'.split()
}

def getRandomWord(wordDict):
    # This function returns a random string from the passed list of strings
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        # Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        # Show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def PlayAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

difficulty = 'X'
while difficulty not in ['E', 'M', 'H']:
    print('Select difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters += guess

        # Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is ' + secretWord + '!')
            print('You have won!')
            gameIsDone = True
    else:
        missedLetters += guess

        # Check if players has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '".')
            gameIsDone = True

    # Ask player if they want to play again only if the game is done
    if gameIsDone:
        if PlayAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
