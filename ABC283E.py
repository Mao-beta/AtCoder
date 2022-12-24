import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    H, W = NMI()
    A = [NLI() for _ in range(H)]
    INF = 10**5
    # i列決めて、直前に反転しているか(j=0/1)、2個前に反転しているか(k=0/1)のときの最小回数
    dp = [[[INF]*2 for _ in range(2)] for _ in range(H+1)]

    # 反転なしなしorありあり
    ok = True
    for w in range(W):
        if w == 0 and A[0][w+1] == A[0][w]:
            continue
        if w == W-1 and A[0][w-1] == A[0][w]:
            continue
        if 0 < w < W-1 and (A[0][w-1] == A[0][w] or A[0][w+1] == A[0][w]):
            continue
        if A[1][w] != A[0][w]:
            ok = False


    if ok:
        dp[2][0][0] = 0
        dp[2][1][1] = 2

    # 反転なしありorありなし
    ok = True
    for w in range(W):
        if w == 0 and A[0][w + 1] == A[0][w]:
            continue
        if w == W - 1 and A[0][w - 1] == A[0][w]:
            continue
        if 0 < w < W - 1 and (A[0][w - 1] == A[0][w] or A[0][w + 1] == A[0][w]):
            continue
        if A[1][w] == A[0][w]:
            ok = False

    if ok:
        dp[2][0][1] = 1
        dp[2][1][0] = 1


    for i in range(2, H):
        now = A[i]
        prev = A[i-1]
        pprev = A[i-2]

        prev_r = [1-x for x in prev]
        pprev_r = [1-x for x in pprev]

        for j in range(2):
            if j:
                P = prev_r
            else:
                P = prev

            for k in range(2):
                if k:
                    PP = pprev_r
                else:
                    PP = pprev

                if dp[i][j][k] == INF: continue

                ok = True
                nj = -1
                for w in range(W):
                    S = [PP[w]]
                    if w > 0:
                        S.append(P[w-1])
                    if w < W-1:
                        S.append(P[w+1])

                    if P[w] in S:
                        continue

                    tmp = int(P[w] != now[w])
                    if nj == -1:
                        nj = tmp
                    elif nj == tmp:
                        continue
                    else:
                        ok = False

                if ok:
                    if nj == -1:
                        dp[i + 1][0][j] = min(dp[i + 1][0][j], dp[i][j][k])
                        dp[i + 1][1][j] = min(dp[i + 1][1][j], dp[i][j][k] + 1)
                    else:
                        dp[i+1][nj][j] = min(dp[i+1][nj][j], dp[i][j][k] + nj)

    # print(*dp, sep="\n")

    for j in range(2):
        for k in range(2):
            P = [x^j for x in A[-1]]
            PP = [x ^ k for x in A[-2]]
            for w in range(W):
                S = [PP[w]]
                if w > 0:
                    S.append(P[w-1])
                if w < W-1:
                    S.append(P[w+1])

                if P[w] not in S:
                    dp[-1][j][k] = INF

    # print(*dp, sep="\n")

    ans = INF
    for j in range(2):
        for k in range(2):
            ans = min(ans, dp[-1][j][k])

    print(ans if ans < INF else -1)



if __name__ == "__main__":
    main()
