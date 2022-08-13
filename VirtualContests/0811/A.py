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
    if N == 1:
        print(1)
        exit()

    ok = 1
    ng = N+10
    while abs(ok-ng) > 1:
        k = (ok+ng)//2
        if k*(k+1)//2 <= N+1:
            ok = k
        else:
            ng = k

    print(N - ok + 1)




if __name__ == "__main__":
    main()
