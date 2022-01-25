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
    T = SI()

    SL = len(S)
    TL = len(T)

    @lru_cache(maxsize=None)
    def edit_distance(i, j):
        if i >= SL: return TL - j
        if j >= TL: return SL - i
        if S[i] == T[j]:
            return edit_distance(i+1, j+1)

        res_add = edit_distance(i, j+1)
        res_del = edit_distance(i+1, j)
        res_mod = edit_distance(i+1, j+1)
        return 1 + min(res_add, res_del, res_mod)

    print(edit_distance(0, 0))


if __name__ == "__main__":
    main()
