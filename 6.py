import sys



for line in sys.stdin.readlines():

    # idx = 3
    for idx in range(3, len(line)):
        # print(set([line[idx], line[idx - 1], line[idx - 2], line[idx - 3]]), len(set([line[idx], line[idx - 1], line[idx - 2], line[idx - 3]])), idx)
        if len(set([line[idx], line[idx - 1], line[idx - 2], line[idx - 3]])) == 4:
            print(idx + 1)
            break