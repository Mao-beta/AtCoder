N, Q = map(int, input().split())
S = input()
LR = [list(map(int, input().split())) for _ in range(Q)]
#dp[i]はi番目までの文字で'AC'がいくつあるか
dp = [0] * (N+1)
for i in range(1, N):
    if S[i-1] == 'A' and S[i] == 'C':
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

for l, r in LR:
    print(dp[r-1] - dp[l-1])
