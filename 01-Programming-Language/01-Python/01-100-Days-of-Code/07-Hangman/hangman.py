import random
import hangman_art
import hangman_words
import os

word_list = hangman_words.word_list
stages = hangman_art.stages

end_of_game = False
lives = 6
pGuess = ""

chosen_word = word_list[random.randint(0,len(word_list)-1)]
print(hangman_art.logo)
print(f"Psst, the solution is {chosen_word}")

display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    state = 0
    if lives > 0:
        guess = input("Guess a letter: ").lower()
        os.system('cls')


        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
                state += 1

        if guess in pGuess:
             print(f"You already guessed {guess}")
        elif state == 0:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
        else:
            print(f"You guessed {guess}, that's correct.")
    
        print(display)
        print(stages[lives])
        pGuess += guess

        if "_" not in display:
            end_of_game = True
            print("You win.")
        
    else:
        print("You LOSE")
        end_of_game = True
    