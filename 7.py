# Hangman Game
import random


ascii_art = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\ |
 / \\ |
      |
=========''']

game_name = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                   
'''

print(game_name)
words = ['house', 'tree', 'ball', 'amazing']
word = random.choice(words)
hidden_word = ['-' for _ in range(len(word))]
wrong_guesses = 0
tries = []

while '-' in hidden_word:

    print(f'Guess the word * {''.join(hidden_word)} *')
    print(f'{ascii_art[wrong_guesses]}\n')
    player_guess = input('Guess a letter: ')

    if player_guess in tries:
        print(f'You already guessed this letter.')
        continue

    elif player_guess in word:
        print(f'Yes! "{player_guess}" is in.')
        for index in range(len(hidden_word)):
            if word[index] == player_guess:
                hidden_word[index] = player_guess

    else:
        print(f'No, "{player_guess}" is not in the word.')
        wrong_guesses += 1
        if wrong_guesses == 6:
            print(f'{ascii_art[wrong_guesses]}\n')
            print('You Lose!')
            print(f'The word was: {word}')
            exit()
    tries += player_guess
print(f'Congratulations, you guessed the word {word}!')
