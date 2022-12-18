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

    l = 1
    r = N + 1
    for i in range(10):
        if r - l <= 1:
            break
        m = (l + r) // 2
        print(f"? {l} {m-1} 1 {N}")
        sys.stdout.flush()
        res = NI()
        if res < m - l:
            r = m
        else:
            l = m

    X = l

    l = 1
    r = N + 1
    for i in range(10):
        if r - l <= 1:
            break
        m = (l + r) // 2
        print(f"? 1 {N} {l} {m-1}")
        sys.stdout.flush()
        res = NI()
        if res < m - l:
            r = m
        else:
            l = m

    Y = l

    print(f"! {X} {Y}")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
