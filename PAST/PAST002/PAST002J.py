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
    S = SI()
    N = len(S)

    def rec(start):
        stock = []
        # print("s", start, stock)
        i = start
        while i < N:
            # print(i, stock)
            s = S[i]
            if s == "(":
                i, res = rec(i+1)
                stock += res
            elif s == ")":
                return i, stock + stock[::-1]
            else:
                stock.append(s)
            i += 1
        return i, stock

    ans = rec(0)[1]
    print("".join(ans))


if __name__ == "__main__":
    main()
