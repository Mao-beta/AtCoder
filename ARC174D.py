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


def solve(N):
    res = 1
    if N < 80:
        return res
    res += 1
    if N < 10**2 - 10:
        return res
    if N < 10**2 + 10:
        return res + N - 90 + 1
    res += 20

    B = 100
    if N < B**2 - B*2:
        return res
    res += 1
    if N < B**2 - B:
        return res
    if N < B**2 + B:
        return res + N - (B**2 - B) + 1
    res += 2*B

    B = 10**3
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10**4
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10**5
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 6
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 7
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 8
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 9
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 10
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 11
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 12
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 13
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 14
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 15
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 16
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 17
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B

    B = 10 ** 18
    if N < B ** 2 - B * 2:
        return res
    res += 1
    if N < B ** 2 - B:
        return res
    if N < B ** 2 + B:
        return res + N - (B ** 2 - B) + 1
    res += 2 * B


def main():
    T = NI()
    for _ in range(T):
        N = NI()
        print(solve(N))


if __name__ == "__main__":
    main()
