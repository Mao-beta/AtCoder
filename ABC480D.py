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

# ライブラリ https://github.com/Mao-beta/AtCoder


def main():
    N, Q = NMI()
    A = NLI()
    C = list(accumulate([0]+A))
    CC = list(accumulate(C))
    D = list(accumulate(range(N+1)))
    # print(C)
    # print(CC)
    # print(D)
    for _ in range(Q):
        L, R = NMI()

        def calc(r):
            idx = bisect.bisect_right(D, r)
            ans = CC[idx-1] + C[r-D[idx-1]]
            return ans

        # print(calc(R), calc(L - 1))
        print(calc(R) - calc(L-1))


if __name__ == "__main__":
    main()
