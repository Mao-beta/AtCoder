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
    D = NI()
    C = NLI()
    costs = C[:]
    score = 0


    def decide_maxcosts():
        return costs.index(max(costs))

    def decide(theta):
        V = S[:]
        for i in range(26):
            V[i] += costs[i] ** theta
        return V.index(max(V))


    for _ in range(D):
        S = NLI()

        # 開催コンテスト決定
        idx = decide(theta=1.2)

        # 開催した種類のコストを0にする
        costs[idx] = 0
        print(idx+1, flush=True)

        # スコア計算TODO
        delta = S[idx] - sum(C)
        score += delta

        # 1日のおわりにコスト増加
        for i, c in enumerate(C):
            costs[i] += c

    print("#", score)


if __name__ == "__main__":
    main()
