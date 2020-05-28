import sys
input = sys.stdin.readline
N, M, Q = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(M)]
PQ = [list(map(int, input().split())) for _ in range(Q)]

#X[l][r]はlからrをちょうど走る電車の数
X = [[0 for _ in range(N+1)] for _ in range(N+1)]
for l, r in LR:
    X[l][r] += 1
cum = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        cum[i][j] = cum[i][j-1] + X[i][j]

outputs = []
for p, q in PQ:
    ans = 0
    for i in range(p, q+1):
        ans += cum[i][q] - cum[i][p-1]
    outputs.append(ans)

print('\n'.join(map(str, outputs)))
