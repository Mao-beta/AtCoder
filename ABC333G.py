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
    r = SI()[2:]
    r = int(r + "0"*(18-len(r))) # r * 10**18
    ten = 10**18
    N = NI()

    # a/b <= p <= c/d を満たす a,b,c,d <= n を求める
    def stern_brocot(p, n):
        la = 0
        lb = 1
        ra = 1
        rb = 0
        lu = ru = 1
        lx = 0
        ly = 1
        rx = 1
        ry = 0

        def f(ma, mb):
            # 左の子か
            return p * mb < ma * ten

        prev = (lx, ly, rx, ry)
        while lu or ru:
            ma = la + ra
            mb = lb + rb
            if f(ma, mb):
                # 指数探索で短縮
                k = 1



                ra = ma
                rb = mb
                if ma <= n and mb <= n:
                    rx = ma
                    ry = mb
                else:
                    lu = 0
            else:
                la = ma
                lb = mb
                if ma <= n and mb <= n:
                    lx = ma
                    ly = mb
                else:
                    ru = 0
            if (lx, ly, rx, ry) == prev:
                break
            prev = (lx, ly, rx, ry)
            print(prev)
        # lx/ly <= p <= rx/ry
        return lx, ly, rx, ry

    lx, ly, rx, ry = stern_brocot(r, N)
    if abs(ly * ry * r - ten * lx * ry) <= abs(ly * ry * r - ten * rx * ly):
        print(lx, ly)
    else:
        print(rx, ry)


if __name__ == "__main__":
    main()
