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
    S = SI()
    W = []
    now = []
    for s in S:
        if s.islower():
            now.append(s)
        elif len(now) == 0:
            now.append(s)
        else:
            now.append(s)
            W.append("".join(now))
            now = []
    # print(W)
    W.sort(key=lambda x: x.lower())
    print("".join(W))


if __name__ == "__main__":
    main()
