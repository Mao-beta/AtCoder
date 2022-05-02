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


def main():
    G = [NLI() for _ in range(4)]
    for h in range(4):
        for w in range(4):
            for dh, dw in [[1, 0], [0, 1]]:
                nh, nw = h+dh, w+dw
                if nh >= 4 or nw >= 4:
                    continue
                if G[h][w] == G[nh][nw]:
                    print("CONTINUE")
                    exit()
    print("GAMEOVER")


if __name__ == "__main__":
    main()
