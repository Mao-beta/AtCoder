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
    M, N = NMI()
    g = math.gcd(M, N)
    M //= g
    N //= g
    ans = 0
    while M > 1 or N > 1:
        if M < N:
            M, N = N, M
            ans += 1
        else:
            d, r = divmod(M, N)
            M = r
            ans += d
            if N == 1:
                ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
