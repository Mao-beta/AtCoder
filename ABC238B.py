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
    A = [0] + NLI()
    C = list(accumulate(A))
    C = [c % 360 for c in C]
    C = sorted(C) + [360]
    ans = 0
    for i in range(len(C)-1):
        ans = max(ans, C[i+1] - C[i])
    print(ans)


if __name__ == "__main__":
    main()
