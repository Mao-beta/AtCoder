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
    N = NI()
    A = NLI()
    X = set()
    now = 0
    X.add(0)
    for a in A:
        now = (now + a) % 360
        X.add(now)
    X.add(min(X)+360)
    X = sorted(list(X))
    ans = 0
    for i in range(len(X)-1):
        ans = max(ans, X[i+1]-X[i])
    print(ans)


if __name__ == "__main__":
    main()
