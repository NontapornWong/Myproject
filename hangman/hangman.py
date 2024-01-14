stages = ['''  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''   
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', ''' 
 +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''' , '''
 +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', ''' 
 +---+
  |   |
  O   |
  |   |
      |
      |
=========
''' , ''' 
 +---+
  |   |
  O   |
      |
      |
      |
=========
''' , ''' 
 +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
# word_list = ["ardvark", "baboon", "camel"]
from hangman_word import word_list

chosen_word = random.choice(word_list)
word_len = len(chosen_word)

end_of_game = False
lives = 6

from hangman_art import logo, stages
print(logo)

print(f"Pssst, the solution is: {chosen_word}")

display = []
for _ in chosen_word:
    display += "_"
print(display)


while not end_of_game:
    guessed = input("Please guess the letter: ").lower()

    if guessed in display:
        print(f"You already guessed {guessed}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed:
            display[position] = letter

    if guessed not in chosen_word:
        print(f"You guessed {guessed}, that not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!!")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!!")
    
    print(stages[lives])

