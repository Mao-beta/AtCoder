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
    N = NI()
    S = SI()
    X = [0] * 10
    for s in S:
        X[int(s)] += 1
    ans = 0
    M = int(10**6.6)
    for i in range(M):
        t = i * i
        Y = [0] * 10
        while t > 0:
            Y[t % 10] += 1
            t //= 10
        ok = True
        for k in range(10):
            if k == 0:
                if X[0] < Y[0]:
                    ok = False
            else:
                if X[k] != Y[k]:
                    ok = False
        if ok:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
