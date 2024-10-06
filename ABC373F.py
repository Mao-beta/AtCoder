import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, W = NMI()
    WV = EI(N)
    W2V = [[] for _ in range(W+1)]
    INF = 10**20
    for w, v in WV:
        for k in range(1, 3001):
            if w * k > W:
                break
            if v-(k*2-1) <= 0:
                break
            W2V[w].append(v-(k*2-1))
    nWV = []
    for w in range(1, W+1):
        num = W // w
        W2V[w] = sorted(W2V[w], reverse=True)[:num]
        nWV += [[w, v] for v in W2V[w]]
    # print(W2V[:10])
    N = len(nWV)
    # print(nWV)
    # 重さiのものまで処理したときに重さjであるときの最高価値
    dp = [[-INF]*(W+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        w, v = nWV[i]
        for j in range(W+1):
            if dp[i][j] < 0:
                continue

            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
            if j+w <= W:
                dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v)
    print(max(dp[-1]))
    # print(*dp, sep="\n")


if __name__ == "__main__":
    main()
