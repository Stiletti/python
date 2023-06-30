print("Welcome to Python Pizza Deliveries !")
size = input("Which size you want ? (S, M, L): ")
add_pepperoni = input("Do you want pepperoni ? (Y/N): ")
extra_cheese = input("Do you want extra cheese ? (Y/N): ")
price = 0

if size == 'S' or size == 's':
    price = 15
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        price += 3
    if extra_cheese == 'Y' or extra_cheese == 'y':
        price += 2

if size == 'M' or size == 'm':
    price = 20
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        price += 3
    if extra_cheese == 'Y' or extra_cheese == 'y':
        price += 2
    
if size == 'L' or size == 'l':
    price = 25
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        price += 3
    if extra_cheese == 'Y' or extra_cheese == 'y':
        price += 2
        
print(f"your final bill is {price} $.")