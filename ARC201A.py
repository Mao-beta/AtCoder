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


def process(a, b, c):
    # ab, bc, free
    if a >= b >= c:
        return b-c, 0, c
    elif a <= b <= c:
        return 0, b-a, a
    elif b >= a + c:
        return a, c, 0
    elif b <= a and b <= c:
        return 0, 0, b
    else:
        return b-c, b-a, a+c-b


def solve(N, ABC):
    AB, BC, FR = 0, 0, 0
    for a, b, c in ABC:
        ab, bc, free = process(a, b, c)
        AB += ab
        BC += bc
        FR += free
    ans = min(AB, BC)
    AB -= ans
    BC -= ans
    rem = AB + BC
    if rem >= FR:
        return ans + FR
    else:
        return ans + rem + (FR-rem) // 2


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        ABC = EI(N)
        ans = solve(N, ABC)
        print(ans)


if __name__ == "__main__":
    main()
