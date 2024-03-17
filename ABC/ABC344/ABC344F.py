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
    N = NI()
    P = EI(N)
    R = EI(N)
    D = EI(N-1)
    INF = 10**15
    
    # C: h,wからゴールまでの最小合計コスト
    C = [[INF]*N for _ in range(N)]
    C[N-1][N-1] = 0
    for h in range(N-1, -1, -1):
        for w in range(N-1, -1, -1):
            if h < N-1:
                C[h][w] = min(C[h][w], C[h+1][w] + D[h][w])
            if w < N-1:
                C[h][w] = min(C[h][w], C[h][w+1] + R[h][w])

    # h,w,pmaxでの最小行動回数とそのときの最大所持金
    dp = [[defaultdict(lambda: [INF, 0]) for _ in range(N)] for _ in range(N)]
    dp[0][0][P[0][0]] = [0, 0]
    ans = INF
    for h in range(N):
        for w in range(N):
            for pmax, (act, money) in dp[h][w].items():
                # ここで全部稼ぐときの答え
                c = C[h][w]
                if money >= c:
                    ans = min(ans, act + N-1-h + N-1-w)
                else:
                    k = (c-money + pmax-1) // pmax
                    ans = min(ans, act + k + N-1-h + N-1-w)

                # 最低限稼いで次へ遷移
                if h < N-1:
                    npmax = max(pmax, P[h+1][w])
                    if money >= D[h][w]:
                        nact = act + 1
                        nmoney = money - D[h][w]
                    else:
                        k = (D[h][w] - money + pmax - 1) // pmax
                        nact = act + k + 1
                        nmoney = money + k * pmax - D[h][w]
                    if nact < dp[h+1][w][npmax][0]:
                        dp[h+1][w][npmax] = [nact, nmoney]
                    elif nact == dp[h+1][w][npmax][0]:
                        dp[h+1][w][npmax][1] = max(dp[h+1][w][npmax][1], nmoney)

                if w < N-1:
                    npmax = max(pmax, P[h][w+1])
                    if money >= R[h][w]:
                        nact = act + 1
                        nmoney = money - R[h][w]
                    else:
                        k = (R[h][w] - money + pmax - 1) // pmax
                        nact = act + k + 1
                        nmoney = money + k * pmax - R[h][w]
                    if nact < dp[h][w+1][npmax][0]:
                        dp[h][w+1][npmax] = [nact, nmoney]
                    elif nact == dp[h][w+1][npmax][0]:
                        dp[h][w+1][npmax][1] = max(dp[h][w+1][npmax][1], nmoney)

    print(ans)


if __name__ == "__main__":
    main()
