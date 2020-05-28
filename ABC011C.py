N = int(input())
NGs = [int(input()) for _ in range(3)]
cnt = 0
if N in NGs:
    print('NO')
    exit()

while N >= 1 and cnt <= 99:
    #print('N=', N)
    if N == 0:
        print('YES')
        exit()

    tmp_3 = N - 3
    tmp_2 = N - 2
    tmp_1 = N - 1
    if tmp_3 not in NGs and tmp_3 >= 0:
        N = N - 3
        cnt += 1
        continue
    if tmp_2 not in NGs and tmp_2 >= 0:
        N = N - 2
        cnt += 1
        continue
    if tmp_1 not in NGs and tmp_1 >= 0:
        N = N - 1
        cnt += 1
        continue
    print('NO')
    exit()

if N == 0:
    print('YES')
else:
    print('NO')
