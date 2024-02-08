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
    N, M = NMI()
    conds = [[] for _ in range(M)]
    for i in range(M):
        k = NI()
        conds[i] = EI(k)

    def judge(case, cond):
        for a, b in cond:
            a -= 1
            if (case>>a) & 1 == b:
                return True
        return False

    for case in range(1<<N):
        ok = True
        for cond in conds:
            if not judge(case, cond):
                ok = False
        if ok:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
