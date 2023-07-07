scores = input("Scores: ").split()
for n in range(0, len(scores)):
    scores[n] = int(scores[n])
print(scores)
        
highest2 = 0
for score in scores:
    if score > highest2:
        highest2 = score

print("Highest 2 = " + str(highest2))