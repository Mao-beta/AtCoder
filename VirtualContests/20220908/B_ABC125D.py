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
    N = NI()
    A = NLI()
    minus = len([a for a in A if a < 0])
    if minus % 2 == 0:
        print(sum([abs(a) for a in A]))
    else:
        target = min(A, key=abs)
        print(sum([abs(a) for a in A]) - abs(target) * 2)


if __name__ == "__main__":
    main()
