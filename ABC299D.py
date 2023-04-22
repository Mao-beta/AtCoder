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
    l = 1
    r = N
    for _ in range(20):
        m = (l+r) // 2
        print(f"? {m}", flush=True)
        x = NI()
        if x == 0:
            l = m
        else:
            r = m

        if r - l == 1:
            break

    print(f"! {l}")


if __name__ == "__main__":
    main()
