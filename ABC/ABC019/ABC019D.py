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
    N = NI()

    u = 1
    res = []
    for v in range(1, N+1):
        if u == v: continue
        print(f"? {u} {v}")
        sys.stdout.flush()
        d = NI()
        res.append([d, v])
    res.sort(reverse=True)

    u = res[0][1]
    res = []
    for v in range(1, N+1):
        if u == v: continue
        print(f"? {u} {v}")
        sys.stdout.flush()
        d = NI()
        res.append([d, v])
    res.sort(reverse=True)

    d = res[0][0]
    print(f"! {d}")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
