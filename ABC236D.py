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
    A = [NLI() for _ in range(2*N-1)]
    AA = [[-1] * 2*N for _ in range(2*N)]
    for i, a in enumerate(A):
        for j, aa in enumerate(a, start=i+1):
            AA[i][j] = aa
            AA[j][i] = aa
    # print(*AA, sep="\n")

    ans = [0]

    def rec(rem, now):
        if not rem:
            ans[0] = max(ans[0], now)
            return

        i = min(rem)
        rem.discard(i)
        for j in rem:
            rec(rem - {j}, now^AA[i][j])

    rec(set(range(2*N)), 0)
    print(ans[0])


if __name__ == "__main__":
    main()
