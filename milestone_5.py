import random

def check_guess(word, word_guessed, guess):
    guess = guess.lower()
    
    if guess in word:
        print(f"Good guess!{guess} is in the word")
        
        for i in range (len(word)):
            if word[i] == guess:
                word_guessed[i] = guess
                return True
            else:
                print(f"Sorry, {guess} is not in the word.")
                return False
            def ask_for_input(word,word_guessed, list_of_guesses):
                while True:
                    guess = input("Guess a letter: ").strip()
                    if len(guess) == 1 and guess.isalpha():
                        guess = guess.lower()
                        if guess in list_of_guesses:
                            print("You already tried that letter!")
                        else:
                            list_of_guesses.append(guess)
                            return guess
                    else:
                        print("Invalid letter.Please, enter a single alphabetical character.")
                        def play_game(word_list):
                            num_lives = 5
                            word = random.choice(word_list)
                            word_guessed = ["_"]*len(word)
                            num_letters = len(set(word))
                            list_of_guesses = []