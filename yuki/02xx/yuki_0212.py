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
    P, C = NMI()
    Dp = [2, 3, 5, 7, 11, 13]
    Dc = [4, 6, 8, 9, 10, 12]
    ans = 0
    cnt = 0
    for X in product(Dp, repeat=P):
        for Y in product(Dc, repeat=C):
            cnt += 1
            tmp = 1
            for x in X:
                tmp *= x
            for y in Y:
                tmp *= y
            ans += tmp
    print(ans / cnt)


if __name__ == "__main__":
    main()
