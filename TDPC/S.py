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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    H, W = NMI()

    def f(b):
        res = []
        for _ in range(H):
            res.append(b % 4)
            b //= 4
        return res

    # bの3進数表示
    bits = [f(b) for b in range(4**H)]
    ok_bs = set()
    for b, bit in enumerate(bits):
        ok = True

        for i in range(H-1):
            bp = bit[i]
            bn = bit[i+1]
            if bp * bn == 0:
                continue
            if bp != bn:
                ok = False

        if 1 not in bit:
            ok = False

        nz = [x for x in bit if x > 0]
        if ok and sorted(nz) != nz:
            ok = False

        if ok and (max(nz) + 1 != len(set(bit))):
            ok = False

        if ok:
            ok_bs.add(b)
            print(bit)

    print(len(bits))
    print(len(ok_bs))

    # dp[i][b]: 左からi列決めて、右端の状態がbの場合の数
    # dp[W][b]のうち、bits[b][-1]=1であるものの総和が答え
    dp = [[0]*(3**H) for _ in range(W+1)]

    for i in range(W):
        pass



if __name__ == "__main__":
    main()
