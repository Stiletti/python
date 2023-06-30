name1 = input("Whats your name ?: ").lower()
name2 = input("Whats your crush's name ?: ").lower()
score1 = 0
score2 = 0
check1 = "true"
check2 = "love"

def checkTrue(name, check1, check2):
    score = 0
    for i in name:
        for j in check1: 
            if i == j:
                score += 1
        for k in check2:
            if i == k:
                score += 1
    return score
    
score1 = checkTrue(name1, check1, check2)
score2 = checkTrue(name2, check1, check2)
            
con_score1 = str(score1)
con_score2 = str(score2)
final_score = int(con_score1 + con_score2)

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos !")
elif final_score > 40 and final_score > 50:
    print(f"Your score is {final_score}, your alright together !")
else:
    print(f"Your score is {final_score}.")