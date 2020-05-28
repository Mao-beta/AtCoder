S = input()
n = len(S)
ATGC = set(['A', 'T', 'G', 'C'])
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        tmp_s = S[i:j]
        if len(set(tmp_s) - ATGC) == 0:
            ans = max(ans, j-i)
print(ans)
