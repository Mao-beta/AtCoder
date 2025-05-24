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
        H, W = NMI()
        S = list(SI())
        d, r = S.count("D"), S.count("R")

        lower = [0] * W
        L = S[:]
        rem = H-1 - d
        nh = 0
        nw = 0
        for i, s in enumerate(L):
            if s == "?":
                if rem > 0:
                    rem -= 1
                    nh += 1
                else:
                    lower[nw] = nh
                    nw += 1
            elif s == "D":
                nh += 1
            else:
                lower[nw] = nh
                nw += 1
        lower[nw] = nh

        upper = [0] * W
        L = S[:]
        rem = W - 1 - r
        nh = 0
        nw = 0
        for i, s in enumerate(L):
            if s == "?":
                if rem > 0:
                    rem -= 1
                    upper[nw+1] = nh
                    nw += 1
                else:
                    nh += 1
            elif s == "D":
                nh += 1
            else:
                upper[nw+1] = nh
                nw += 1

        # print(upper)
        # print(lower)
        ans = 0
        for l, u in zip(lower, upper):
            ans += l-u+1
        print(ans)


if __name__ == "__main__":
    main()
