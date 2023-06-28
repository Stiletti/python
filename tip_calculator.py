price = float(input("How much was the meal ?: "))
number_persons = int(input("How much people ?: "))
tax = float(input("How much tax ?: "))

result = (price / number_persons) * (tax / 100)
print("Tax to pay per person: " + str(round(result, 2)))