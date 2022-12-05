import sys




answer = 0

for line in sys.stdin:
    first, second = line.split(",")

    firstRange = range(int(first.split("-")[0]), int(first.split("-")[1]) + 1)
    secondRange = range(int(second.split("-")[0]), int(second.split("-")[1]) + 1)

    # if second range is within first range or first range is within second range
    if (firstRange[0] <= secondRange[0] and firstRange[-1] >= secondRange[-1]) or (secondRange[0] <= firstRange[0] and secondRange[-1] >= firstRange[-1]):
        answer += 1

    
print(answer)