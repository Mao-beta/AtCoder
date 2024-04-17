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


def _solve(S):
    gmax = S.count("G")
    rmax = S.count("R")
    if gmax != rmax:
        return False
    ok = True
    w = 0
    g = 0
    for s in S:
        if s == "G":
            if w == 0:
                ok = False
                break
            gmax -= 1
            g += 1
        elif s == "R":
            rmax -= 1
            if g and w:
                g -= 1
                w -= 1
            else:
                ok = False
                break
        else:
            if rmax == 0 or gmax == 0:
                ok = False
                break
            w += 1
    if g:
        ok = False
    return ok


def solve(S):
    S = S[::-1]
    r = 0
    g = 0
    w_ok = False
    for s in S:
        if s == "R":
            r += 1
        elif s == "G":
            if r == 0:
                return False
            r -= 1
            g += 1
            w_ok = True
        else:
            if g:
                g -= 1
            elif not w_ok:
                return False
    if g or r:
        return False
    return True


def main():
    T = NI()
    for _ in range(T):
        S = SI()
        if solve(S):
            print("possible")
        else:
            print("impossible")

def guchoku():
    for P in product("WGR", repeat=6):
        ok = solve(P)
        if P[0] != "W":
            assert not ok, P
            continue
        if P[-1] != "R":
            assert not ok, P
            continue
        if P.count("G") != P.count("R"):
            assert not ok, P
            continue
        print("".join(P))
        if ok:
            print("possible")
        else:
            print("impossible")


if __name__ == "__main__":
    main()
    # guchoku()
