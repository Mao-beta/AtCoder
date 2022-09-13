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
    SA = deque(list(SI()))
    SB = deque(list(SI()))
    SC = deque(list(SI()))
    pl = 0
    S = [SA, SB, SC]
    while True:
        SS = S[pl]
        if len(SS) == 0:
            print("ABC"[pl])
            exit()

        pl = "abc".index(SS.popleft())


if __name__ == "__main__":
    main()
