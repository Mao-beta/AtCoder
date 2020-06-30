N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    CA = list(map(int, input().split()))
    C.append(CA[0])
    A.append(CA[1:])

buys = []
for i in range(2**N):
    buy = []
    for j in range(N):
        if ((i>>j) & 1):
            buy.append(j)
    buys.append(buy)

ans = 10**9
flag = 1
for books in buys:
    cost = 0
    power = [0] * M
    for book in books:
        cost += C[book]
        for i in range(M):
            power[i] += A[book][i]

    if min(power) >= X:
        ans = min(ans, cost)
        flag = 0

print(-1 if flag else ans)