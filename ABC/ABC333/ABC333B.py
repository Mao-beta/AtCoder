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
    s1, s2 = SI()
    t1, t2 = SI()
    s = abs(ord(s1) - ord(s2))
    t = abs(ord(t1) - ord(t2))
    if s == t or s == 5-t:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
