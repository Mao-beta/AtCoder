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
    N = NI()
    S = [SI() for _ in range(N)]
    G = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if S[i][-1] == S[j][0]:
                G[i].append(j)
    print(G)

    def rec(now, bit):
        bit |= 1 << now
        print(now, bin(bit))
        # ここから先手として勝てるか
        win = False
        for v in G[now]:
            if (bit >> v) & 1:
                continue

            nextwin = rec(v, bit | (1 << v))
            if not nextwin:
                win = True

        print(now, bin(bit), win)
        return win


    for start in range(N):
        win = rec(start, 0)
        if win:
            print("First")
            return

    print("Second")


if __name__ == "__main__":
    main()
