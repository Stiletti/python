heights = [156, 177, 186, 192, 158, 167, 182]
heights_len = len(heights)
score = 0

for i in heights:
    score += i
    
result = round(score / heights_len)

print(f"Average is {result}")