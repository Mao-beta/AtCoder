import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, M = NMI()
    ans = []

    def rec(r):
        # 残r
        if len(X) < N and X[-1] >= M:
            return
        if len(X) == N:
            ans.append(X[:])
            return
        for nx in range(r+1):
            X.append(X[-1]+10+nx)
            rec(r-nx)
            X.pop()

    for a1 in range(1, M+1):
        X = [a1]
        R = M - 10 * (N - 1) - a1
        if R < 0:
            break
        rec(R)

    print(len(ans))
    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
