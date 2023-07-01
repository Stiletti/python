row1 = ["+++", "+++", "+++"]
row2 = ["+++", "+++", "+++"]
row3 = ["+++", "+++", "+++"]

map = [row1, row2, row3]

place_treasure = input("Where you wanna place the treasure ?: ")
column = int(place_treasure[0])
row = int(place_treasure[1])

map[column -1][row -1] = "X"

print(f"{row1}\n{row2}\n{row3}")
