height = float(input("Enter ur height in m: "))
weight = float(input("Enter ur weight in Kg: "))

result = round(weight / (height ** 2), 2)

if result < 18.5:
    print(f"Your BMI is {result} , you are underweighted !")
    
if result >= 18.5 and result <= 25:
    print(f"Your BMI is {result} , you have normal weight.")
    
if result > 25 and result <= 30:
    print(f"Your BMI is {result} , you are overweighted !")

if result > 30 and result <= 35:
    print(f"Your BMI is {result} , you are obese !")
    
if result > 35:
    print(f"Your BMI is {result} , you are clinical obese !") 