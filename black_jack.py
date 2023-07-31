"""
    Black Jack logic:
    =================
    1. Give player and AI cards
    2. Player cards and AI will be sum up separate
    3. Ask player for more cards and let AI choose if it wants more cards
    4. If player reaches 21 and is higher than AI - WIN
    5. If player comes over 21 or player score is lower than AI score - LOSE
    6. Ask the player he wants to play again
"""

import random


def give_cards():
    card_counter = 0
    cards_list = ["Jack", "Queen", "King"]
    output_list = []
    while card_counter < 2:
        random_number = random.randint(2, 11)

        if random_number == 10:
            choose_card = random.randint(0, len(cards_list) - 1)
            output_list.append(cards_list[choose_card])
            card_counter += 1
            continue

        if random_number == 11:
            output_list.append("Ace")
            card_counter += 1
            continue

        output_list.append(random_number)
        card_counter += 1

    return output_list


def sum_of_cards(card_list, high_cards_dic):
    sum_of_all = 0
    for card in card_list:
        if card not in high_cards_dic:
            sum_of_all += card
        else:
            for key in high_cards_dic:
                if key == card:
                    sum_of_all += high_cards_dic[key]

    return sum_of_all


def add_card(card_list):
    random_number = random.randint(2, 11)
    cards_list = ["Jack", "Queen", "King"]

    if random_number == 10:
        choose_card = random.randint(0, len(cards_list) - 1)
        card_list.append(cards_list[choose_card])
    elif random_number == 11:
        card_list.append("Ace")
    else:
        card_list.append(random_number)


high_cards = {
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11
}


player_cards = give_cards()
player_value = sum_of_cards(player_cards, high_cards)

ai_cards = give_cards()
ai_value = sum_of_cards(ai_cards, high_cards)

print(f"Player cards: {player_cards} with value of {player_value} , AI cards: {ai_cards} with value of {ai_value}")

total_score_player = 0
total_score_ai = 0
win = False
while not win:
