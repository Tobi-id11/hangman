import random
secret_words=["apple","banana","orange","strawberry","kiwi"]
def check_guess(guess,word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess!{guess} is in he word.")
    else:
        print(f"sorry,{guess} is not in the word.Try again")
        def ask_for_input():
            while True:
                guess = input("Guess a letter:")
                if len(guess) == 1 and guess.isalpha():
                    return guess
                print("Invalid letter.Please, enter a single alphabetical character.")
                while True:
                    secret_word = random.choice(secret_words)
                    guess = ask_for_input()
                    
                    check_guess(guess,secret_word)