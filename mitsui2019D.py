N = int(input())
S = input()
ans = 0
for i in range(1000):
    i = str(i).zfill(3)
    match = 0
    idx = 0
    for s in S:
        if i[idx] == s:
            match += 1
            idx += 1
        if match == 3:
            break
    if match == 3:
        ans += 1
print(ans)