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
    N = NI()
    A = NLI()
    ans = [10**20]

    def rec(state, M, m):
        # print(bin(state)[2:].zfill(3*N), M, m)
        first = -1
        for i in range(3*N):
            if (state >> i) & 1 == 0:
                first = i
                break
        if first == -1:
            ans[0] = min(ans[0], M-m)
            # print(first, state, M, m, ans[0])
            return
        for second in range(first+1, 3*N):
            if (state >> second) & 1:
                continue
            for third in range(second + 1, 3 * N):
                if (state >> third) & 1:
                    continue
                ns = state | (1<<first) | (1<<second) | (1<<third)
                s = A[first] + A[second] + A[third]
                rec(ns, max(M, s), min(m, s))

    rec(0, 0, 10**20)
    print(ans[0])


if __name__ == "__main__":
    main()
