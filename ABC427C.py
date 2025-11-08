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
    UV = EI(M)
    UV = [[x-1, y-1] for x, y in UV]
    ans = 10**12
    for P in product(range(2), repeat=N):
        tmp = 0
        for u, v in UV:
            if P[u] == P[v]:
                tmp += 1
        # print(P, tmp)
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
