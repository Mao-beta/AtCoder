N = int(input())
dp = [[0, 0] for _ in range(N+1)]
dp[2] = [13, 3]
MOD = 10**9 + 7
for i in range(3, N+1):
    dp[i][0] = (dp[i-1][0] * 43 + dp[i-1][1] * 9) % MOD
    dp[i][1] = (dp[i-1][0] * 9 + dp[i-1][1] * 3) % MOD

print((dp[N][0] + dp[N][1])%MOD)