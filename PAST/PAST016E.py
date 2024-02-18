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
    X = SI()
    ans = len(X)
    just = 1
    for i, x in enumerate(X):
        if i == 0 and x == "1":
            continue
        if i > 0 and x == "0":
            continue
        just = 0
    if just:
        ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
