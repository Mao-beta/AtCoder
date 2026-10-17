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
    N, W = NMI()
    AB = EI(N)
    AB.sort()
    rem = W
    ans = 0
    for a, b in AB[::-1]:
        if rem >= b:
            ans += a * b
            rem -= b
        else:
            ans += rem * a
            break
    print(ans)


if __name__ == "__main__":
    main()
