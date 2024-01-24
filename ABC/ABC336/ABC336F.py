import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product, chain

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
    S = EI(H)
    S = list(chain.from_iterable(S))


    def rev(base, sh, sw):
        base = list(base)
        sumh = 2*sh + H-2
        sumw = 2*sw + W-2
        cnt = 0
        for h in range(sh, sh+H-1):
            for w in range(sw, sw+W-1):
                if cnt >= ((H-1)*(W-1)+1) // 2:
                    break
                hh = sumh - h
                ww = sumw - w
                idx = h*W + w
                ridx = hh*W + ww
                base[idx], base[ridx] = base[ridx], base[idx]
                cnt += 1
            if cnt >= ((H - 1) * (W - 1) + 1) // 2:
                break

        return base

    SH = [0, 0, 1, 1]
    SW = [0, 1, 0, 1]

    SS = [set() for _ in range(11)]
    SS[0].add(tuple(S))
    for i in range(10):
        for T in SS[i]:
            for sh, sw in zip(SH, SW):
                res = tuple(rev(T, sh, sw))
                if res not in SS[i]:
                    SS[i+1].add(res)

    R = tuple(range(1, H*W+1))
    RS = [set() for _ in range(11)]
    RS[0].add(tuple(R))
    for i in range(10):
        for T in RS[i]:
            for sh, sw in zip(SH, SW):
                res = tuple(rev(T, sh, sw))
                if res not in RS[i]:
                    RS[i+1].add(res)

    ans = 100
    for i in range(11):
        for j in range(11):
            if SS[i] & RS[j]:
                ans = min(ans, i+j)
    print(ans if ans <= 20 else -1)


if __name__ == "__main__":
    main()
