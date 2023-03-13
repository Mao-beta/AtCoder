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
    M, K = NMI()

    if K >= 2**M:
        print(-1)
        return

    if M == 0:
        print(0, 0)
        return

    if M == 1:
        if K == 0:
            print(0, 0, 1, 1)
        else:
            print(-1)
        return

    A = set(range(2**M))
    A.discard(K)
    A = list(A)
    ans = [K] + A + [K] + A[::-1]
    print(*ans)


if __name__ == "__main__":
    main()
