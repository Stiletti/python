age = int(input("Your age: "))
expectation = 80
months_left = (expectation * 12) - (age * 12)
weeks_left = (expectation * 12 * 4) - (age * 12 * 4)
days_left = (expectation * 12 * 4 * 7) - (age * 12 * 4 * 7)

print(f"By average of 80 years you have {months_left} months, {weeks_left} weeks and {days_left} days left.") 