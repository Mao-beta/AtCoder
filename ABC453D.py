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
    H, W = NMI()
    S = [SI() for _ in range(H)]
    shw = [0, 0]
    ghw = [0, 0]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "S":
                shw = [h, w]
            elif S[h][w] == "G":
                ghw = [h, w]
    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    def f(d, h, w):
        return d*H*W + h*W + w

    def g(dhw):
        dh, w = divmod(dhw, W)
        d, h = divmod(dh, H)
        return d, h, w

    dp = [0] * (4*H*W)
    D = "RLDU"

    pars = [4*H*W] * (4*H*W)

    stack = deque()
    for d in range(4):
        stack.append([d, *shw]) # d, h, w

    while stack:
        d, h, w = stack.pop()
        # print(d, h, w)
        if h == ghw[0] and w == ghw[1]:
            ans = []
            dhw = f(d,h,w)
            while not (h == shw[0] and w == shw[1]):
                dhw = pars[dhw]
                d, h, w = g(dhw)
                ans.append(D[d])
            ans = ans[::-1]
            print("Yes")
            print("".join(ans))
            return

        if dp[f(d,h,w)]:
            continue
        dp[f(d, h, w)] = 1

        dh, dw = DH[d], DW[d]
        nh, nw = h+dh, w+dw
        if nh < 0 or nw < 0 or nh >= H or nw >= W:
            continue
        if S[nh][nw] == "#":
            continue

        for nd in range(4):
            if S[nh][nw] == "o" and d != nd:
                continue
            if S[nh][nw] == "x" and d == nd:
                continue
            if dp[f(nd,nh,nw)]:
                continue
            pars[f(nd,nh,nw)] = f(d,h,w)
            stack.append([nd, nh, nw])

    print("No")


if __name__ == "__main__":
    main()
