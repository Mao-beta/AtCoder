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
    P = [a for a in A if a >= 0]
    M = [a for a in A if a < 0]
    if len(M) == 0:
        ans = min(A) * sum(A) - min(A) ** 2
        print(ans)
        return
    if len(P) == 0:
        ans = max(A) * sum(A) - max(A) ** 2
        print(ans)
        return

    ans = max(P) * sum(M) + sum(P) * min(M) - max(P) * min(M)
    print(ans)


if __name__ == "__main__":
    main()
