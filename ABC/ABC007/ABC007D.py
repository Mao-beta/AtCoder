A, B = map(int, input().split())

def forbidden(n):
    # dp[i][j]はNの上からi桁目(0-origin)まで決まっていてN未満不確定/確定(j=0,1)のときの場合の数
    n_str = str(n)
    dp = [[0, 0] for _ in range(len(n_str) + 1)]
    dp[0][0] = 1
    for i in range(len(n_str)):
        digit = int(n_str[i])
        for d in range(digit+1):
            if d == 4 or d == 9:
                continue
            if d == digit:
                dp[i+1][0] += dp[i][0]
            else:
                dp[i+1][1] += dp[i][0]
        dp[i+1][1] += dp[i][1] * 8
    return n - sum(dp[len(n_str)])

print(forbidden(B) - forbidden(A-1))