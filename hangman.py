import random
import os

__author__ = 'Omri'

NUMBER_OF_TRIES = 7
NUMBER_OF_CATAGORIES = 2


def main():
    random_word = get_random_word(enter_choice())
    already_entered = []
    tries = NUMBER_OF_TRIES
    print("Let's start... You have {} guess!".format(tries))
    while tries is not 0:
        user_input = input("Enter Letter: ")
        user_input = user_input.lower()
        if user_input.isalpha() and len(user_input) is 1:
            if user_input not in already_entered:
                already_entered.append(user_input)
                if user_input in random_word:
                    print("Good Guess!")
                    if print_already_found(random_word, already_entered) is True:
                        break
                else:
                    tries -= 1
                    print("Bad guess! you have {} tries left.".format(tries))
            else:
                print("You already tried this letter..")
        else:
            print("Please enter only letters")
    if tries is 0:
        print("You Lost!")


def print_already_found(the_word, the_guess):
    counter = 0
    for letter in the_word:
        if letter in the_guess or letter == '&' or letter == ' ':
            print(letter, end="")
            counter += 1
        else:
            print("_", end="")
    print('\n')
    if counter == len(the_word):
        print("YOU WIN!")
        return True


def enter_choice():
    while True:
        num = input("Please enter the category you want\nYou can choose from: 1- Fruits, 2-Countries: ")
        try:
            new_num = int(num)
            if 1 <= new_num <= NUMBER_OF_CATAGORIES:
                break
            else:
                raise Exception
        except Exception:
            pass
    return num


def get_random_word(num):
    path = os.path.dirname(os.path.realpath("hangman.py"))
    path += '\\'
    if int(num) is 1:
        load_path = path + 'fruits.txt'
    elif int(num) is 2:
        load_path = path + 'countries.txt'
    with open(load_path, 'r') as word_bag:
        my_list = [line for line in word_bag]
    my_list = [word.strip().lower() for word in my_list]
    return my_list[random.randint(0, len(my_list) - 1)]


if __name__ == "__main__":
    main()
