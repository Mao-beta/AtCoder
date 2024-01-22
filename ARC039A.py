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
    A, B = NMI()
    ans = A - B
    ans = max(ans, A % 100 + 900 - B)
    ans = max(ans, A // 100 * 100 + A % 10 + 90 - B)
    ans = max(ans, A // 10 * 10 + 9 - B)
    ans = max(ans, A - (B % 100 + 100))
    ans = max(ans, A - (B // 100 * 100 + B % 10))
    ans = max(ans, A - (B // 10 * 10))
    print(ans)


if __name__ == "__main__":
    main()
