import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
from datetime import datetime, timedelta

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
    D = datetime.strptime(S, "%Y/%m/%d")
    delta = timedelta(days=1)
    for i in range(366 * 1000):
        d = datetime.strftime(D, "%Y/%m/%d")
        # print(d)
        if len(set(d)) <= 3:
            print(d)
            exit()
        D += delta



if __name__ == "__main__":
    main()
