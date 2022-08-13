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
    H, W = NMI()
    A = [NLI() for _ in range(H)]
    H2, W2 = NMI()
    B = [NLI() for _ in range(H2)]

    for h_case in range(1<<H):
        if bin(h_case).count("1") != H2: continue
        hs = [i for i in range(H) if (h_case >> i) & 1]

        for w_case in range(1<<W):
            if bin(w_case).count("1") != W2: continue

            ws = [i for i in range(W) if (w_case >> i) & 1]

            ok = True
            for h2, h1 in enumerate(hs):
                for w2, w1 in enumerate(ws):
                    if A[h1][w1] != B[h2][w2]:
                        ok = False

            if ok:
                print("Yes")
                exit()

    print("No")


if __name__ == "__main__":
    main()
