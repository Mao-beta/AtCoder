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
    X = SI()
    L = len(X)

    for k in range(int(X[0]), 10):
        for g in range(-9, 10):
            ans = [k]
            for i in range(L-1):
                ans.append(ans[-1] + g)

            if any([a < 0 or a >= 10 for a in ans]):
                continue

            A = int("".join(map(str, ans)))
            if A >= int(X):
                print(A)
                exit()


if __name__ == "__main__":
    main()
