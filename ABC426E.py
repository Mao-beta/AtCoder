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
        tsx, tsy, tgx, tgy = NMI()
        asx, asy, agx, agy = NMI()
        lt2 = (tgx - tsx) ** 2 + (tgy - tsy) ** 2
        la2 = (agx - asx) ** 2 + (agy - asy) ** 2
        if lt2 < la2:
            tsx, tsy, tgx, tgy, asx, asy, agx, agy = asx, asy, agx, agy, tsx, tsy, tgx, tgy
            lt2, la2 = la2, lt2
        # lt >= la
        lt = math.sqrt(lt2)
        la = math.sqrt(la2)

        def func(t):
            tx = tsx + t * (tgx - tsx) / lt
            ty = tsy + t * (tgy - tsy) / lt
            if t <= la:
                ax = asx + t * (agx - asx) / la
                ay = asy + t * (agy - asy) / la
            else:
                ax, ay = agx, agy
            d = (tx - ax) ** 2 + (ty - ay) ** 2
            return math.sqrt(d)

        left, right = 0.0, la
        # print("#", left, right)

        for _ in range(100):

            # 真ん中の値を計算
            mi1 = (2 * left + right) / 3
            mi2 = (left + 2 * right) / 3
            # print(mi1, func(mi1))
            # print(mi2, func(mi2))

            # 狭める方向を判定(条件式の不等号は適宜変更)
            if func(mi1) > func(mi2):
                left = mi1
            else:
                right = mi2

        ans = func(left)

        left, right = la, lt
        # print("#", left, right)

        for _ in range(100):

            # 真ん中の値を計算
            mi1 = (2 * left + right) / 3
            mi2 = (left + 2 * right) / 3
            # print(mi1, func(mi1))
            # print(mi2, func(mi2))

            # 狭める方向を判定(条件式の不等号は適宜変更)
            if func(mi1) > func(mi2):
                left = mi1
            else:
                right = mi2

        ans = min(ans, func(left))
        print(ans)


if __name__ == "__main__":
    main()
