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
    X = NI()
    if X <= 10:
        print(X)
        return
    S = set()
    for x in range(1, 10):
        for d in range(-9, 10):
            now = x
            nx = x
            while now <= 10**18:
                S.add(now)
                nx += d
                if nx < 0 or 9 < nx:
                    break
                now = now * 10 + nx
                # print(now)
    S = sorted(list(S))
    for s in S:
        if s >= X:
            print(s)
            return


if __name__ == "__main__":
    main()
