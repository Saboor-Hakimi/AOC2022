import sys



for line in sys.stdin.readlines():

    # idx = 3
    for idx in range(14, len(line)):
        # print(set([line[idx], line[idx - 1], line[idx - 2], line[idx - 3]]), len(set([line[idx], line[idx - 1], line[idx - 2], line[idx - 3]])), idx)
        
        st = set()

        for i in range(idx, idx - 14, -1):
            st.add(line[i])
        if len(st) == 14:
            print(idx + 1)
            break