import sys
from itertools import accumulate


MOD = 10 ** 9 + 7
MOD99 = 998244353

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, K = NLI()
    A = NLI()
    dpR = [[0]*(K+2) for _ in range(N+1)]
    dpR[N][1] = 1

    for i in range(N, 0, -1):
        a = A[i-1]
        for j in range(1, K+2):
            if dpR[i][j]:
                dpR[i-1][j] = 1
                nj = min(j+a, K+1)
                dpR[i-1][nj] = 1

    ans = 0
    dpL = [0] * (K+1)
    dpL[0] = 1
    for i in range(N):
        dpL2 = [0] * (K+1)
        for j in range(K+1):
            dpR[i+1][j+1] += dpR[i+1][j]
        a = A[i]
        # jに対して、j+x<K and j+x+a>=K なるxが存在するか？
        # K-j-a <= x < K-j
        ng = True
        for j in range(K):
            if dpL[j]:
                dpL2[j] = 1
                nj = min(j + a, K)
                dpL2[nj] = 1

                l = max(0, K-j-a)
                r = K-j
                if (dpR[i+1][r] - dpR[i+1][l]) > 0:
                    ng = False
        ans += int(ng)
        dpL = dpL2

    print(ans)


if __name__ == "__main__":
    main()
