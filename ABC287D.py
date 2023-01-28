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


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    S = SI()
    T = SI()
    top = 0
    for s, t in zip(S, T):
        if s == "?" or t == "?":
            top += 1
        elif s == t:
            top += 1
        else:
            break

    bottom = 0
    for s, t in zip(S[::-1], T[::-1]):
        if s == "?" or t == "?":
            bottom += 1
        elif s == t:
            bottom += 1
        else:
            break

    for x in range(len(T)+1):
        if x <= top and len(T)-x <= bottom:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
