import words
import random
from hangman_logo import logo, stages
print(logo)
chosen_word = random.choice(words.word_list)
print(f'Pssst, the solution is not very hard.')
lives = 7
x = []
for char in chosen_word:
    x += "_" 
while '_' in x and lives != 0:
  guess = input("Guess a letter: ").lower()
  if guess in x:
      print(f"You've already guessed {guess}")
  elif guess in chosen_word:
      for a in range(0, len(chosen_word)):
          if guess == chosen_word[a]:
              x[a] = guess
  elif guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life")
      lives -= 1
      print(stages[lives])
  print(f"{' '.join(x)}")
if lives == 0:
    print("game over")
else:
    print("you win")