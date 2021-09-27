import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = SI()
    K = len(N)

    # dp[i][j][k][l]
    # i桁まで確定 jは未満フラグ lは前4桁[0000,9999] kは51?3を含むか
    dp = [[[0]*10000 for _ in range(4)]
          for _ in range(K+1)]
    dp[0][0][0] = 1

    for i in range(K):
        for j in range(2):
            for k in range(2):
                jk = j*2 + k
                for l in range(10000):
                    lim = 9 if j == 1 else int(N[i])
                    for x in range(lim+1):
                        nj = j | (x < lim)
                        nl = (l % 1000) * 10 + x
                        nk = k | (nl//100 == 51 and nl%10 == 3)
                        njk = nj*2 + nk

                        dp[i+1][njk][nl] += dp[i][jk][l]

    ans = 0
    for j in range(2):
        for l in range(10000):
            ans += dp[K][j*2+1][l]

    print(ans)


if __name__ == "__main__":
    main()
