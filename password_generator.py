import random

uppercase_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                     "S", "T", "U", "V", "W", "X", "Y", "Z"]

lowercase_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                     "s", "t", "u", "v", "w", "x", "y", "z"]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

special_characters = ["!", "?", "&", "#", "/"]

choice_uppercase_letters = int(input("How many capital letters you wanna have ?: "))
choice_lowercase_letters = int(input("How many lowercase letters you wanna have ?: "))
choice_numbers = int(input("How many numbers you wanna have ?: "))
choice_special_chars = int(input("How many special characters you wanna have ?: "))

pw_length = choice_uppercase_letters + choice_lowercase_letters + choice_numbers + choice_special_chars
pw = []


def get_letters(choice, list_to_check):
    if choice > 0:
        while choice > 0:
            random_number = random.randint(0, len(list_to_check) - 1)
            for n in range(0, len(list_to_check)):
                if n == random_number:
                    pw.append(list_to_check[n])
                    choice -= 1


def make_str_pw(password):
    pw_str = ""
    for n in range(0, len(password)):
        if password[n] != str:
            password[n] = str(password[n])
            pw_str += password[n]
    return pw_str


def randomize_pw(password):
    # convert pw into str to make a save for the used pw possible
    make_str_pw(password)
    # create variable for used rand number
    used_rand_num = 0
    # create variable for used item
    used_item = ""
    # create for loop with range to access all items of the list
    for n in range(0, len(password)):
        # create rand int to switch letters index
        rand_int = random.randint(0, len(password) - 1)
        # set item into item variable
        used_item = password[n]
        # set rand number into rand variable...
        # ...maybe
        # give item randon number as index
        password[n] = password[rand_int]
        # set item variable for index of random number
        password[rand_int] = used_item


get_letters(choice_uppercase_letters, uppercase_letters)
get_letters(choice_lowercase_letters, lowercase_letters)
get_letters(choice_numbers, numbers)
get_letters(choice_special_chars, special_characters)

print(pw)
randomize_pw(pw)

print(make_str_pw(pw))
