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
    N, Q = NMI()
    A = NLI()
    A.sort()
    ans = [0] * Q
    for qi in range(Q):
        x, y = NMI()
        msx = bisect.bisect_left(A, x)

        ok = 10**10
        ng = x-1
        while abs(ok - ng) > 1:
            m = (ok + ng) // 2
            total = m - (x - 1)
            a = bisect.bisect_right(A, m) - msx
            if total - a >= y:
                ok = m
            else:
                ng = m

        ans[qi] = ok
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
