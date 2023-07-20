alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
text = input("Type in your massage: ").lower()
shift = int(input("Number to shift: "))


def encrypt(shift_num, shift_text, shift_alphabet):
    text_list = []
    for letter in shift_text:
        text_list.append(letter)

    # replace the letter from shift_text with the index offset letter from shift_alphabet
    outgoing_text = ""
    for n in range(0, len(text_list)):
        for m in range(0, len(shift_alphabet)):
            if text_list[n] == shift_alphabet[m]:
                outgoing_text += shift_alphabet[m+shift_num]

    return outgoing_text


def decrypt(shift_num, shift_text, shift_alphabet):
    text_list = []
    for letter in shift_text:
        text_list.append(letter)

    # replace the letter from shift_text with the index offset letter from shift_alphabet
    outgoing_text = ""
    for n in range(0, len(text_list)):
        for m in range(0, len(shift_alphabet)):
            if text_list[n] == shift_alphabet[m]:
                outgoing_text += shift_alphabet[m - shift_num]

    return outgoing_text


if direction == "encrypt":
    print(encrypt(shift, text, alphabet))
else:
    print(decrypt(shift, text, alphabet))
