import os

bidders = {}

new_bidder = True
while new_bidder:
    name = input("Enter your name: ")
    bid = float(input("Your bid: "))
    bidders[name] = bid
    more_bidders = input("More bidders (y/n) ?: ")

    if more_bidders == 'n' or more_bidders == 'N':
        new_bidder = False

    if more_bidders == 'y' or more_bidders == 'Y':
        # clear console
        # to ge this to work enable edit in terminal output console next to the debug button
        os.system("clear")

highest_bid = 0.0
highest_bidder = ""
for bid in bidders:
    if bidders[bid] > highest_bid:
        highest_bid = bidders[bid]
        highest_bidder = bid

print(f"Highest bidder was {highest_bidder} with {highest_bid}$ - GZ !")
