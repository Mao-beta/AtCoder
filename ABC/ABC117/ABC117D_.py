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
    N, K = NMI()
    A = NLI()

    INF = 1<<60
    K = bin(K)[2:].zfill(40)
    L = len(K)
    # dp[i][j] 上からi桁bitまで確定 jは未満フラグ のときの最大のf
    dp = [[-INF]*2 for _ in range(L+1)]
    dp[0][0] = 0

    for i in range(L):
        for j in range(2):
            lim = 1 if j == 1 else int(K[i])
            for x in range(lim+1):
                nj = j | (x < lim)
                tmp = 0
                for a in A:
                    tmp += (((a>>(L-1-i))&1) ^ x) << (L-1-i)
                dp[i+1][nj] = max(dp[i+1][nj], dp[i][j] + tmp)

    print(max(dp[L]))


if __name__ == "__main__":
    main()
