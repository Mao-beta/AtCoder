import sys

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
    N = NI()
    C = [0] * 5000
    for _ in range(N):
        C[NI()] += 1
    # dp[i]: i個以上NG
    dp = [0] * (N+1)
    dp[0] = 1
    for i in range(N):
        for j in range(N-1, -1, -1):
            dp[j+1] += dp[j] * C[i] % MOD
            dp[j+1] %= MOD
    fac = [1] * (N+1)
    for i in range(1, N+1):
        fac[i] = fac[i-1] * i % MOD
    ans = 0
    for i in range(N+1):
        ans += dp[i] * fac[N-i] * (i%2*(-2)+1) % MOD
        ans %= MOD
    print(ans % MOD)


if __name__ == "__main__":
    main()
