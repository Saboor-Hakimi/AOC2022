import sys




answer = 0

for line in sys.stdin:
    first, second = line.split(",")

    firstRange = range(int(first.split("-")[0]), int(first.split("-")[1]) + 1)
    secondRange = range(int(second.split("-")[0]), int(second.split("-")[1]) + 1)

    for i in firstRange:
        if i in secondRange:
            answer += 1
            break
    

    
print(answer)