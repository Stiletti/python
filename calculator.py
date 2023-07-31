# calc functions

# addition
def addition(nr1, nr2):
    return nr1 + nr2


# subtraction
def subtraction(nr1, nr2):
    return nr1 - nr2


# division
def division(nr1, nr2):
    return nr1 / nr2


# multiplication
def multiplication(nr1, nr2):
    return nr1 * nr2


def format_output(nr1, nr2, operation, op_dic):
    print(f"{nr1} {operation} {nr2} = {op_dic[operation](nr1, nr2)}")
    # op_dic[operation] returns the function, so we can give it parameters (nr1, nr2)
    return op_dic[operation](nr1, nr2)


operation_dic = {
    '+': addition,
    '-': subtraction,
    '/': division,
    '*': multiplication
}

number1 = int(input("Type nr1: "))
choice = True

while choice:
    number2 = int(input("Type next nr: "))

    for key in operation_dic:
        print(key)

    symbol = input("What you wanna do ? : ")

    result = format_output(number1, number2, symbol, operation_dic)

    choice = input(f"Wanna calc with {result} (y/n) ? : ")
    if choice == 'n' or choice == 'N':
        choice = False
        print("See you later !")
    else:
        number1 = result
