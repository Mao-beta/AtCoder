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
    a, b, S = SMI()
    if S[-2] != ".":
        S = S + ".0"
    S = S.replace(".", "")
    # print(S)
    S = int(S.split("UTC")[1]) - 90
    S *= 6
    h, m = divmod(S, 60)
    a, b = int(a), int(b)
    a += h
    b += m
    if b < 0:
        b += 60
        a -= 1
    if b >= 60:
        b -= 60
        a += 1
    # print(h, m, a, b)
    a %= 24
    print(f"{a:02d}:{b:02d}")


if __name__ == "__main__":
    main()
