import random

words = []
best_guess = []
tries = int(input("How many tries ?: "))
counter = 0
num_words = int(input("How many Words you wanna guess? : "))

while len(words) < num_words:
    word = input("Word: ")
    words.append(word)


def get_word_from_list(list_name):
    rand_int = random.randint(0, len(list_name) - 1)
    for y in range(0, len(list_name)):
        if y == rand_int:
            return list_name[y]


def create_word(guessing_word, player_guess):
    guessed_word = []
    for x in range(0, len(word_to_guess)):
        if player_guess == guessing_word[x]:
            guessed_word.append(guessing_word[x])
        else:
            guessed_word.append("_")
    return guessed_word


word_to_guess = get_word_from_list(words)
wtg_list = []

for letter in word_to_guess:
    wtg_list.append(letter)

while counter < tries:

    if wtg_list == best_guess:
        print("YOU WIN !")
        break

    guess = input("\nGuess a letter: ")
    word = create_word(word_to_guess, guess)
    counter += 1

    if len(best_guess) < len(word_to_guess):
        best_guess = word

    for n in range(0, len(best_guess)):
        if word[n] != best_guess[n] and word[n] != "_":
            best_guess[n] = word[n]

    best_guess_str = ""
    for m in best_guess:
        best_guess_str += m

    print("Tries left: " + str(tries - counter))
    print("Your guess: " + best_guess_str)
    print("==========================================")

else:
    print("YOU LOSE !")
