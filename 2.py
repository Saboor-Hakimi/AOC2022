import sys


def rock_paper_scissors(A,B):
    if A == B:
        return 0
    elif A == "rock" and B == "scissors":
        return 1
    elif A == "rock" and B == "paper":
        return -1
    elif A == "paper" and B == "rock":
        return 1
    elif A == "paper" and B == "scissors":
        return -1
    elif A == "scissors" and B == "paper":
        return 1
    elif A == "scissors" and B == "rock":
        return -1
    
    

score = 0
codes = {"A": "X", "B": "Y", "C": "Z"}
nums = {"X": 1, "Y": 2, "Z": 3}
mapping = {"A": "X", "B": "Y", "C": "Z"}
dmap = {"X": 'rock', "Y": 'paper', "Z": 'scissors'}

for line in sys.stdin:
    first, second = line.split()

    temp = 0
    
    res =  rock_paper_scissors(dmap[mapping[first]], dmap[second])
    temp += nums[second]
    if res == 0:
        temp += 3
    elif res == 1:
        temp += 0
    elif res == -1:
        temp += 6
    score += temp

    # print(temp)
    # print(score)
    
print(score)
        
    


    