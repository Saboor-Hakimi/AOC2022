#     [C]             [L]         [T]
#     [V] [R] [M]     [T]         [B]
#     [F] [G] [H] [Q] [Q]         [H]
#     [W] [L] [P] [V] [M] [V]     [F]
#     [P] [C] [W] [S] [Z] [B] [S] [P]
# [G] [R] [M] [B] [F] [J] [S] [Z] [D]
# [J] [L] [P] [F] [C] [H] [F] [J] [C]
# [Z] [Q] [F] [L] [G] [W] [H] [F] [M]
#  1   2   3   4   5   6   7   8   9 

S1 = ["Z", "J", "G"]
S2 = ["Q", "L", "R", "P", "W", "F", "V", "C"]
S3 = ["F", "P", "M", "C", "L", "G", "R"]
S4 = ["L", "F", "B", "W", "P", "H", "M"]
S5 = ["G", "C", "F", "S", "V", "Q"]
S6 = ["W", "H", "J", "Z", "M", "Q", "T", "L"]
S7 = ["H", "F", "S", "B", "V", "V"]
S8 = ["F", "J", "Z", "S"]
S9 = ["M", "C", "D", "P", "F", "H", "B", "T"]


stacks = []
for i in range(1, 10):
    stacks.append(eval("S" +str(i)))


# print(stacks)

import sys


for line in sys.stdin.readlines():
    parts = line.split()
    amount = int(parts[1])
    firstStack = int(parts[3])
    secondStack = int(parts[5])
    
    # get amount elements from the end of the first stack
    # and put them on the second stack
    
    tmp = []
    for i in range(amount):
        if len(stacks[firstStack - 1]) > 0:
            # dont pop from the firstStack, append it with the same order
            tmp.append(stacks[firstStack - 1].pop())

    # now put the elements from the tmp list on the second stack
    for i in range(len(tmp)):
        stacks[secondStack - 1].append(tmp.pop())
        
            
for stack in stacks:
    if len(stack) > 0:
        print(stack[-1], end = "")
print()
        
    
