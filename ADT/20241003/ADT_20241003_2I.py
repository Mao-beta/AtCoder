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
    N, H = NMI()
    TD = EI(N)
    TD.sort(key=lambda x: -x[1])
    h = 0
    day = 0
    prevtd = 0
    for t, d in TD:
        if t * d <= prevtd:
            continue
        # prevtdを超えるタイミング
        xday = (prevtd + d-1) // d - 1
        hadd = prevtd * (xday - day)
        hadd2 = d * (day+1 + t) * (t - day) // 2
        if h + hadd >= H:
            ans = (H-h + prevtd-1) // prevtd + day
            print(ans)
            return
        h += hadd
        if h + hadd2 >= H:
            def judge(X):
                ha = d * (day + 1 + X) * (X - day) // 2
                return h + ha >= H

            ok = t+1
            ng = xday
            while abs(ok - ng) > 1:
                X = (ok + ng) // 2
                if judge(X):
                    ok = X
                else:
                    ng = X

            print("#", ok)
            return

        h += hadd2
        prevtd = t * d
        day = t

    print()


if __name__ == "__main__":
    main()
