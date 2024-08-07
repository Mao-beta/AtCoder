import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def solve(A, B, C):
    if A > B:
        A, B = B, A
    if C < B:
        return 0
    if C > B+1:
        return 0
    # A <= B <= C <= B+1
    if A == B == C:
        res = (1 + 8*pow(10, A-1, MOD99)) * pow(10, A-1, MOD99) * 4 % MOD99
    elif A == B and C == B+1:
        res = (pow(10, A-1, MOD99) * 10 - 1) * pow(10, A-1, MOD99) * 4 % MOD99 + pow(10, A-1, MOD99) ** 2 % MOD99 * 9
    elif C == B:
        res = 9*9 * pow(10, A+B-2, MOD99) % MOD99
        res -= (pow(10, A-1, MOD99) + pow(10, A, MOD99) - 1) * 9 * pow(10, A-1, MOD99) % MOD99 * pow(2, MOD99-2, MOD99) % MOD99
        res %= MOD99
    elif C == B+1:
        res = (pow(10, A-1, MOD99) + pow(10, A, MOD99) - 1) * 9 * pow(10, A-1, MOD99) % MOD99 * pow(2, MOD99-2, MOD99) % MOD99
    else:
        return 0
    return res % MOD99


def guchoku(A, B, C):
    res = 0
    for x1 in range(10**(A-1), 10**A):
        for x2 in range(10**(B-1), 10**B):
            if 10**(C-1) <= x1 + x2 < 10**C:
                res += 1
    return res % MOD99

def main():
    T = NI()
    for _ in range(T):
        A, B, C = NMI()
        res = solve(A, B, C)
        print(res)

def check():
    for A in range(1, 4):
        for B in range(1, 4):
            for C in range(1, 9):
                ans = solve(A, B, C)
                gu = guchoku(A, B, C)
                assert ans == gu, [A, B, C, ans, gu]


if __name__ == "__main__":
    main()
