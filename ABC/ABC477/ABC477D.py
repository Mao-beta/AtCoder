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
    N, Q = NMI()
    B = [[] for _ in range(N)]
    CT = [0]
    CC = ["a"]
    for t in range(1, Q+1):
        q, s = SMI()
        q = int(q)
        if q == 1:
            x = int(s)-1
            B[x].append(t)
        else:
            CT.append(t)
            CC.append(s)

    ans = ["a" for _ in range(N)]
    for i, Bi in enumerate(B):
        Bi.append(10**7)
        # print(i, Bi)
        for j, bij in enumerate(Bi):
            if j % 2 == 0:
                idx = bisect.bisect_left(CT, bij)
                ct, cc = CT[idx-1], CC[idx-1]
                if j > 0 and ct < Bi[j-1]:
                    continue
                # print(i, Bi, j, bij, ct, cc)
                ans[i] = cc
    print(*ans, sep="")


if __name__ == "__main__":
    main()
