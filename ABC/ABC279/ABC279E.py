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
    N, M = NMI()
    A = NLI()

    one = 1
    for a in A:
        if one == a:
            one += 1
        elif one == a+1:
            one -= 1

    X = list(range(N + 1))
    ans = []
    for a in A[::-1]:
        if one == a:
            one += 1
        elif one == a+1:
            one -= 1
        ans.append(X[one])
        X[a], X[a+1] = X[a+1], X[a]

    print(*ans[::-1], sep="\n")


if __name__ == "__main__":
    main()
