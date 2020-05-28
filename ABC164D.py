import heapq
S = input()
cum = [0 for _ in range(len(S))]
dict = {}
length = len(S)
n = 0
for i in range(1,length+1):
    n = n + int(S[-i]) * 10**(i-1)
    cum[i-1] = n % 2019
    dict[cum[i-1]] = 0

for c in cum:
    dict[c] += 1
ans = 0
for k, v in dict.items():
    if k == 0:
        ans += v
    ans += v * (v-1) // 2

print(ans)