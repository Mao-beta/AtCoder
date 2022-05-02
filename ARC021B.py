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
    L = NI()
    B = [NI() for _ in range(L)]

    ans = []
    x = 0
    for b in B:
        ans.append(x)
        x ^= b

    if x != 0:
        print(-1)
        exit()

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
