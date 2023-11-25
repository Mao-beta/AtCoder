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
    A = NLI()
    X = []
    ans = 0
    for a in A:
        if a > 1:
            while X and X[-1] != a-1:
                X.pop()
            if X:
                X[-1] += 1
                ans += len(X)
        else:
            X.append(1)
            ans += len(X)

    print(ans)


if __name__ == "__main__":
    main()
