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
    C = list(accumulate([0] + A + A))
    S = sum(A)
    ans = 10**20

    for i in range(N):
        a = C[i]
        b = a + S // 2
        j = bisect.bisect_left(C, b)

        X = C[j] - a
        Y = S - X
        ans = min(ans, abs(X - Y))

    print(ans)


if __name__ == "__main__":
    main()
