N = int(input())
p = list(map(int, input().split()))
skip = False
ans = 0
for i, a in enumerate(p):
    i = i + 1
    if skip:
        skip = False
        continue
    if i == a:
        ans += 1
        skip = True
print(ans)