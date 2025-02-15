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
    S = SI() * 2
    N = len(S) // 2
    ans = -10**20
    for i in range(N):
        T = S[i:i+N]
        if T[0] in "+-" or T[-1] in "+-":
            continue
        res = 0
        tmp = 0
        pm = 1
        for s in T:
            if s == "+":
                res += tmp * pm
                tmp = 0
                pm = 1
            elif s == "-":
                res += tmp * pm
                tmp = 0
                pm = -1
            else:
                tmp = tmp * 10 + int(s)
        res += tmp * pm
        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
