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
    N = NI()
    Q = NLI()
    A = NLI()
    B = NLI()
    ans = 0
    for m in range(10**6+1):
        R = [Q[i]-A[i]*m for i in range(N)]
        if min(R) < 0:
            break
        tmp = 10**6
        for r, b in zip(R, B):
            if b == 0:
                continue
            if r < b:
                tmp = 0
            else:
                tmp = min(tmp, r//b)
        ans = max(ans, m + tmp)
    print(ans)


if __name__ == "__main__":
    main()
