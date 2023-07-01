import random

pics = [
("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
,
("""
      ______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
,
("""
        ___
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
]

#create random number for ai choice
ai_choice = random.randint(1, 3)

#create player choice
player_choice = int(input("Choose a number (Rock = 1 / Paper = 2 / Scissors = 3): "))

#conditions
if ai_choice == 1 and player_choice == 2 or ai_choice == 2 and player_choice == 3 or ai_choice == 3 and player_choice == 1:
    print(f"\nComputer: \n{pics[ai_choice - 1]}\n\nPayer: \n{pics[player_choice - 1]}\n YOU WIN !") 
elif ai_choice == player_choice:
    print(f"\nComputer: \n{pics[ai_choice - 1]}\n\nPayer: \n{pics[player_choice - 1]}\n DRAW !") 
else:
    print(f"\nComputer: \n{pics[ai_choice - 1]}\n\nPayer: \n{pics[player_choice - 1]}\n YOU LOSE !") 