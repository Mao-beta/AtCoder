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
    C = Counter(A)

    ans = 1

    if N % 2:
        for i in range(0, N, 2):
            val = 1 if i == 0 else 2
            if C[i] != val:
                print(0)
                exit()

            ans = ans * val % MOD

    else:
        for i in range(1, N, 2):
            val = 2
            if C[i] != val:
                print(0)
                exit()

            ans = ans * val % MOD

    print(ans)


if __name__ == "__main__":
    main()
