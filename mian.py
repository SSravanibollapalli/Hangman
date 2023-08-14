import random
import hangman_art
import hangman_words


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)



chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
lst = []
for l in chosen_word:
  lst.append(l)
# print(lst)

display = []
for l in range(word_length):
  l = "_"
  display += l
if lives != 0:
  while display != lst:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You have already guessed {guess}")
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter      
    print(display)
    if guess not in display:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      print(hangman_art.stages[lives])
    if lives == 0: 
      print("You Lose")
      break
  
if display == lst:
  print("You Win")