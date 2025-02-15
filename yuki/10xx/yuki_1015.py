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
    N, *X = NMI()
    A = NLI()
    A = [-a for a in A]
    heapify(A)
    while A:
        a = heappop(A)
        a = -a
        if X[2] > 0:
            if a < 10000:
                X[2] -= 1
                continue

            k, r = divmod(a, 10000)
            if X[2] >= k:
                X[2] -= k
                heappush(A, -r)
                continue
            else:
                heappush(A, -(a-10000*X[2]))
                X[2] = 0
                continue

        if X[1] > 0:
            if a < 5000:
                X[1] -= 1
                continue

            k, r = divmod(a, 5000)
            if X[1] >= k:
                X[1] -= k
                heappush(A, -r)
                continue
            else:
                heappush(A, -(a - 5000 * X[1]))
                X[1] = 0
                continue

        if X[0] > 0:
            if a < 1000:
                X[0] -= 1
                continue

            k, r = divmod(a, 1000)
            if X[0] >= k:
                X[0] -= k
                heappush(A, -r)
                continue
            elif 0 < X[0] < k:
                heappush(A, -(a - 1000 * X[0]))
                X[0] = 0
                continue

        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
