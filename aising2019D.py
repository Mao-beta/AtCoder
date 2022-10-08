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
    N, Q = NMI()
    A = NLI()
    X = [NI() for _ in range(Q)]
    # 偶数/奇数番目の累積和
    Even = list(accumulate([0]+A[::2]))
    Odd = list(accumulate([0]+A[1::2]))
    C = list(accumulate([0]+A))

    B = [a+0.1 for a in A]

    def solve(x):
        if x >= A[-2]:
            if N % 2:
                return Even[-1]
            else:
                return Odd[-1]

        # xから見てg以内のものを全部取る(k個とする)
        # そのとき先手は上からk個とっている
        # これが衝突しないギリギリを二分探索

        def judge(g):
            l = bisect.bisect_left(B, x-g)
            r = bisect.bisect_right(B, x+g)
            k = r - l
            return r <= N - k


        ok = 0
        ng = A[-1]

        while abs(ok - ng) > 0.01:
            g = (ok + ng) / 2
            if judge(g):
                ok = g
            else:
                ng = g


        l = bisect.bisect_left(B, x - ok)
        r = bisect.bisect_right(B, x + ok)
        k = r - l

        aoki = C[r] - C[l]
        if N % 2:
            aoki += Odd[N//2 - k]
        else:
            aoki += Even[N//2 - k]

        res = C[-1] - aoki

        return res



    for x in X:
        res = solve(x)
        print(res)


if __name__ == "__main__":
    main()
