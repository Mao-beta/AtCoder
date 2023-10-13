import sys
from collections import deque, defaultdict, Counter

MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, K = NMI()
    A = [NI() for _ in range(N)]
    C = Counter(A)
    M = 1<<17
    dp = [0] * M
    dp[0] = 1
    dp2 = [0] * M
    for i, (a, c) in enumerate(C.items()):
        p = pow(2, c-1, MOD)
        for j in range(M):
            dp2[j] += dp[j] * p % MOD
            dp2[j] %= MOD
            dp2[j^a] += dp[j] * p % MOD
            dp2[j^a] %= MOD
        dp, dp2 = dp2, dp
        for j in range(M):
            dp2[j] = 0
    print(dp[K])


if __name__ == "__main__":
    main()
