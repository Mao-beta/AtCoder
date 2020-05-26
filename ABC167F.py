N = int(input())
S = []
for i in range(N):
    S.append(input())

S_mod = []
for i, s in enumerate(S):
    tmp = [0,0]
    for k in s:
        if k == ')':
            idx = 0
        else:
            idx = 1
        if idx:
            tmp[idx] += 1
        else:
            if tmp[1-idx] >= 1:
                tmp[1-idx] -= 1
            else:
                tmp[idx] += 1

    if tmp != [0, 0]:
        S_mod.append(tmp)

gap = 0
rflag = 0
lflag = 0
for s in S_mod:
    gap += s[0] - s[1]
    if s[0] == 0 and s[1] >= 1:
        rflag = 1
    if s[0] >= 1 and s[1] == 0:
        lflag = 1

if gap == 0 and lflag and rflag:
    print('Yes')
else:
    print('No')