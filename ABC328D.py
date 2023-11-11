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
    S = SI()
    D = deque()
    for s in S:
        D.append(s)
        if len(D) >= 3 and D[-1] == "C" and D[-2] == "B" and D[-3] == "A":
            D.pop()
            D.pop()
            D.pop()
    print("".join(list(D)))


if __name__ == "__main__":
    main()
