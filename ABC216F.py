import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    B = NLI()

    AE = [(a, i) for i, a in enumerate(A)]
    AE.sort()
    AA = []
    BB = []
    for a, i in AE:
        AA.append(A[i])
        BB.append(B[i])

    # dp[i][j] Bをi個めまで見てかつi個目を使っており、和がjの組の数
    dp = [[0]*5001 for _ in range(N+1)]
    # cum[j] dp[*][j]の累積和
    cum = [0] * 5001

    dp[0][0] = 1
    cum[0] = 1
    for i in range(1, N+1):
        b = BB[i-1]
        for j in range(5001):
            if j >= b:
                dp[i][j] = cum[j-b] % MOD
        for j in range(5001):
            cum[j] += dp[i][j]
            cum[j] %= MOD
    ans = 0
    for i, a in enumerate(AA, start=1):
        ans += sum(dp[i][:a+1])
    print(ans % MOD)


if __name__ == "__main__":
    main()
