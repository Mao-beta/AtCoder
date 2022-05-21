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
    N, L = NMI()
    A = NLI()
    if L > sum(A):
        A.append(L - sum(A))
    heapify(A)
    ans = 0

    while len(A) > 1:
        x = heappop(A)
        y = heappop(A)
        ans += x + y
        heappush(A, x+y)

    print(ans)


if __name__ == "__main__":
    main()
