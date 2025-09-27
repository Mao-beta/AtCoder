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
    T = NI()
    for _ in range(T):
        N = NI()
        P = NLI()
        ans = [0] * (1<<N)
        # print(N, P)

        def rec(l, r, pl, pr):
            # print(l, r, pl, pr)
            if r-l == 1:
                ans[l] = P[pl]
                return
            m = (l+r) // 2
            pm = (pl+pr) // 2
            minlm = min(P[pl:pm])
            minrm = min(P[pm:pr])
            if minlm < minrm:
                rec(l, m, pl, pm)
                rec(m, r, pm, pr)
            else:
                rec(l, m, pm, pr)
                rec(m, r, pl, pm)

        rec(0, 1<<N, 0, 1<<N)
        print(*ans)


if __name__ == "__main__":
    main()
