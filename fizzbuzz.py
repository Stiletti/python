#number divisible by 3 = fizz
#number divisible by 5 = buzz
#number divisible by both = fizzbuzz

for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print(str(number) + " = FizzBuzz !")
        else:
            print(str(number) + " = Fizz !")
    if number % 5 == 0:
        print(str(number) + " = Buzz !")