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
    A = NLI()
    ans = []
    for i in range(N-1):
        x, y = A[i], A[i+1]
        if x < y:
            for a in range(x, y):
                ans.append(a)
        else:
            for a in range(x, y, -1):
                ans.append(a)
    ans.append(A[-1])
    print(*ans)


if __name__ == "__main__":
    main()
