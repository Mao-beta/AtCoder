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
    S = [SI() for _ in range(H)]
    T = [SI() for _ in range(H)]
    
    SC = []
    TC = []
    
    for w in range(W):
        col_s = []
        col_t = []
        for h in range(H):
            s = 1 if S[h][w] == "#" else 0
            t = 1 if T[h][w] == "#" else 0
            col_s.append(s)
            col_t.append(t)
        SC.append(tuple(col_s))
        TC.append(tuple(col_t))
    
    SC = Counter(SC)
    TC = Counter(TC)

    # print(SC)
    # print(TC)

    if SC == TC:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
