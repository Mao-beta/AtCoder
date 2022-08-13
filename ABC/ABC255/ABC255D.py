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
    N, Q = NMI()
    A = NLI()
    X = [NLI() + [i] for i in range(Q)]

    A.sort()

    C = list(accumulate(A[::-1]))[::-1] + [0]
    RA = [-a for a in A]
    RC = [0] + list(accumulate(RA))

    for x, i in X:
        idx = bisect.bisect_left(A, x)
        # print(idx)
        # print(RC[idx], C[idx], x * (N - idx))
        ans = RC[idx] + C[idx] - x * (N - idx) + x * idx
        print(ans)


if __name__ == "__main__":
    main()
