import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
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
    N = SI()
    B = 127
    # dp[i][j][k] 現在の桁和がiで、modjで整数nの余りkのときの場合の数
    # dp[i][i][0]の和が答え
    dp_less = [[[[0]*(B+1) for _ in range(B+1)] for _ in range(B+1)] for _ in range(len(N)+1)]
    dp_notless = [[[[0]*(B+1) for _ in range(B+1)] for _ in range(B+1)] for _ in range(len(N)+1)]

    for m in range(1, B):
        dp_notless[0][0][m][0] = 1

    for si, s in enumerate(N):
        s = int(s)
        P = 10**(len(N)-si-1)
        sni = si+1
        for i in range(B):
            for j in range(1, B):
                for k in range(j):
                    # less -> less
                    for x in range(10):
                        ni = i + x
                        if ni >= B:
                            continue
                        nj = j
                        nk = (k + x * P) % j
                        dp_less[sni][ni][nj][nk] += dp_less[si][i][j][k]

                    # not -> less
                    for x in range(s):
                        ni = i + x
                        if ni >= B:
                            continue
                        nj = j
                        nk = (k + x * P) % j
                        dp_less[sni][ni][nj][nk] += dp_notless[si][i][j][k]

                    # not -> not
                    for x in range(s, s+1):
                        ni = i + x
                        if ni >= B:
                            continue
                        nj = j
                        nk = (k + x * P) % j
                        dp_notless[sni][ni][nj][nk] += dp_notless[si][i][j][k]

    ans = 0
    for i in range(1, B):
        ans += dp_less[-1][i][i][0]
        ans += dp_notless[-1][i][i][0]
    print(ans)


if __name__ == "__main__":
    main()
