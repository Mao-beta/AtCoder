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
    H, W, N = NMI()
    T = SI()
    S = [SI() for _ in range(H)]
    D = {s:i for i, s in enumerate("LRUD")}
    DH = [0, 0, -1, 1]
    DW = [-1, 1, 0, 0]
    ans = 0
    for sh in range(H):
        for sw in range(W):

            def check(sh, sw):
                h, w = sh, sw
                if S[h][w] == "#":
                    return False
                for s in T:
                    d = D[s]
                    h += DH[d]
                    w += DW[d]
                    if S[h][w] == "#":
                        return False
                return True

            if check(sh, sw):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
