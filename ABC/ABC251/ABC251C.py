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
    N = NI()
    D = dict()
    ans = -1
    ans_i = -1
    for i in range(N):
        s, t = SMI()
        t = int(t)
        if not D.get(s):
            D[s] = t
            if ans < t:
                ans = t
                ans_i = i+1

    print(ans_i)


if __name__ == "__main__":
    main()
