number = int(input("Number to check: "))


def prime_number_check(number_to_check):
    if number_to_check % 2 == 0 and number_to_check != 2:
        print(str(number_to_check) + " is not a prime number !")
    else:
        print(str(number_to_check) + " is a prime number !")


prime_number_check(number)