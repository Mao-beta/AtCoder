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
    N, M = NMI()
    S = SI()
    T = SI()

    if T not in S:
        print("No")
        exit()

    # i個見て、最後に置いたのが(0: prefix, 1: suffix, 2: T, 3: 中間)であるのが可能か？
    # 答えはdp[N][1] or dp[N][2]
    #
    dp = [[0]*4 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            # print(i, j, dp[i][j])
            if dp[i][j] == 0:
                continue
            for l in range(M):
                for r in range(l+1, M+1):
                    if l == 0 and r == M:
                        nj = 2
                    elif l == 0:
                        nj = 0
                    elif r == M:
                        nj = 1
                    else:
                        nj = 3

                    if j == 0 or j == 3:
                        if nj == 1 or nj == 3:
                            continue

                    t = T[l:r]
                    ni = i + r-l
                    if ni > N:
                        continue
                    if S[i:ni] != t:
                        continue
                    # print(i, j, ni, nj, S[i:ni], t)
                    dp[ni][nj] = 1

    # print(*dp, sep="\n")

    if dp[N][1] or dp[N][2]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
