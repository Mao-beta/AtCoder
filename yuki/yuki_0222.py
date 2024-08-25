import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    S = SI()

    op = ""
    idx = 0
    for i, s in enumerate(S[1:], start=1):
        if s in "+-":
            op = s
            idx = i
            break
    if op == "+":
        print(int(S[:idx]) - int(S[idx+1:]))
    else:
        print(int(S[:idx]) + int(S[idx + 1:]))


if __name__ == "__main__":
    main()
