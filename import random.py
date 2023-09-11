import random

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.nim_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations.You won the game!")
            break
if __name__ =="__main__":
    play_game(["apple","banana","cherry"])