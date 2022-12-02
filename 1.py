# while there is data in stdin

import sys



elves_cap = []
temp = []

for line in sys.stdin:
    if line == "\n":
        elves_cap.append(temp)
        temp = []
    else:
        temp.append(int(line))
    
# print(elves_cap)
sums = []
for i in elves_cap:
    sums.append(sum(i))

temp = sums.sort()
ans = sums[-1] + sums[-2] + sums[-3]

print(ans)