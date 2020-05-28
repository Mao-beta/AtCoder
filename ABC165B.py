X = int(input())
yen = 100
for i in range(1, 4000):
    yen *= 1.01
    yen = yen // 1
    if yen >= X:
        print(i)
        exit()