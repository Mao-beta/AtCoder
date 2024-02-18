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
    A = NLI()
    D = deque()
    D.append([0, 0])
    total = 0
    for a in A:
        if D[-1][0] == a:
            if D[-1][1] == a-1:
                D.pop()
                total -= a-1
            else:
                D[-1][1] += 1
                total += 1
        else:
            D.append([a, 1])
            total += 1
        print(total)


if __name__ == "__main__":
    main()
