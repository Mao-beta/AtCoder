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


def main():
    N, M = NMI()
    B = NLI()
    W = NLI()
    B.sort(reverse=True)
    W.sort(reverse=True)
    ans = 0
    tmp = 0
    b, w = 0, 0
    while b < N and B[b] >= 0:
        tmp += B[b]
        b += 1
    ans = max(ans, tmp)
    for i in range(M):
        tmp += W[i]
        w += 1
        while b < N and B[b] >= 0:
            tmp += B[b]
            b += 1
        while b < N and b < w:
            tmp += B[b]
            b += 1
        if b < w:
            break
        ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
