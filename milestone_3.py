import random
word_list =["apple","banana","orange","strawberry","kiwi"]
word = random.choice(word_list)

def check_guess(guess,word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess!{guess} is in he word.")
    else:
        print(f"sorry,{guess} is not in the word.Try again")

        
def ask_for_input():
    while True:
        guess = input("Guess a letter:")
        if len(guess) == 1 and guess.isalpha()==True:
                    break
        else:
            print("Invalid letter.Please, enter a single alphabetical character.")
    check_guess(guess)
ask_for_input()