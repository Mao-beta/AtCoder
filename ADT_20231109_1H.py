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
    L = Counter()
    R = Counter(A)
    same = 0
    ans = 0
    for i, a in enumerate(A):
        R[a] -= 1
        same -= L[a]
        ans += same
        same += R[a]
        L[a] += 1

    for a in range(1, N+1):
        k = L[a]
        ans -= k * (k-1) * (k-2) // 6

    print(ans)


if __name__ == "__main__":
    main()
