import random

number_of_persons = int(input("Number of Persons: "))
persons = []

for i in range(number_of_persons):
    i = input("Name: ")
    persons.append(i)
    
random_number = random.randint(0, number_of_persons -1)

print(persons[random_number] + " have to pay !")