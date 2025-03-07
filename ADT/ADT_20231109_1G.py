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
    N, M = NMI()
    ans = 10**18
    for a in range(1, 10**6+1):
        if a > N:
            break
        b = (M + a-1) // a
        if b > N:
            continue
        if b < a:
            break
        ans = min(ans, a * b)
    print(ans if ans < 10**18 else -1)



if __name__ == "__main__":
    main()
