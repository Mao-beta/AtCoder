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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    N, M, Y, Z = NMI()
    CP = [SLI() for _ in range(M)]
    C2i = {}
    C2p = {}
    for i, (c, p) in enumerate(CP):
        C2i[c] = i
        C2p[c] = int(p)

    B = SI()
    R = runLengthEncode(B)
    # print(R)

    INF = 10**18
    N = len(R)

    # dp[i][j]: i個みて色の集合がjで最後の色がk
    dp = [[[-INF]*(M+1) for _ in range(1<<M)] for _ in range(N+1)]
    dp[0][0][M] = 0

    for i in range(N):
        c, x = R[i]
        ci = C2i[c]
        cp = C2p[c]
        for j in range(1<<M):
            for k in range(M+1):
                d = dp[i][j][k]
                if d <= -INF:
                    continue

                # print(i, j, k, d, c, ci, cp)
                # 使わない
                ni = i+1
                nj = j
                nk = k
                dp[ni][nj][nk] = max(dp[ni][nj][nk], d)
                # 使う
                # 前回と同じ色
                if ci == k:
                    ni = i+1
                    nj = j | (1<<ci)
                    nk = ci
                    # 1個積む
                    plus = cp + Y
                    dp[ni][nj][nk] = max(dp[ni][nj][nk], d + plus)
                    # 全部積む
                    plus = (cp + Y) * x
                    dp[ni][nj][nk] = max(dp[ni][nj][nk], d + plus)
                # 違う色
                else:
                    ni = i+1
                    nj = j | (1<<ci)
                    nk = ci
                    # 1個積む
                    plus = cp
                    dp[ni][nj][nk] = max(dp[ni][nj][nk], d + plus)
                    # 全部積む
                    plus = cp + (cp+Y) * (x-1)
                    dp[ni][nj][nk] = max(dp[ni][nj][nk], d + plus)

    ans = 0
    for j in range(1<<M):
        # print(dp[N][j])
        for k in range(M):
            z = Z if j == (1<<M)-1 else 0
            ans = max(ans, dp[N][j][k] + z)

    print(ans)



if __name__ == "__main__":
    main()
