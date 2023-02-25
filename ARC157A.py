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


def main(N, A, B, C, D):
    if abs(B - C) > 1:
        return False
    elif B == C == 0 and A > 0 and D > 0:
        return False
    else:
        return True


if __name__ == "__main__":
    N, A, B, C, D = NMI()
    if main(N, A, B, C, D):
        print("Yes")
    else:
        print("No")
