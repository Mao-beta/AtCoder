N, M = map(int, input().split())
for i,m in enumerate(range(M, 0, -1)):
    if m % 2:
        i = i // 2
        print(str(i+1) + " " + str(i+1+m))
    else:
        i = i // 2
        print(str(N - i - m) + " " + str(N - i))