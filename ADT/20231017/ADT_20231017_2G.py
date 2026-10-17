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
    S = SI()
    D = deque()
    l = 0
    for s in S:
        if l > 0 and s == ")":
            while D[-1] != "(":
                D.pop()
            D.pop()
            l -= 1
        else:
            D.append(s)
            if s == "(":
                l += 1
    print("".join(list(D)))


if __name__ == "__main__":
    main()
