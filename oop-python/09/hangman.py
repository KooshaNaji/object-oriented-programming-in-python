import random

def show_blanks(choosed_word, blank_dict):
    print("word = ")
    for char in choosed_word:
        print(blank_dict[char], end=' ')
    print('')

def hangman():
    guess_chance = 4
    words = ["python", "programming", "hangman", "computer", "keyboard", "developer"]
    choosed_word = random.choice(words)
    # print(choosed_word)
    blank_dict = {}
    for char in choosed_word:
        blank_dict[char] = '-'

    while True:
        print(f'chances: {guess_chance}')
        if guess_chance == 0:
            print('you looser!!!')
            break
        if '-' not in blank_dict.values():
            print('you won!!!')
            break
        show_blanks(choosed_word, blank_dict)
        input_char = input("Enter your suggested character: ")
        if input_char in choosed_word:
            print("True!!!\n\n\n\n")
            blank_dict[input_char] = input_char
        else:
            print("wrong input!!!\n\n\n\n")
            guess_chance -= 1

if __name__ == "__main__":
    hangman()