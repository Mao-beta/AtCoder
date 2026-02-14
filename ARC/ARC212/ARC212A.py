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
    K = NI()
    ans = 0
    for ab in range(2, K):
        for cd in range(2, K):
            ef = K - ab - cd
            if ef < 2:
                continue
            tmp = (ab-1) * (cd-1) * (ef-1) * min(ab+cd, cd+ef, ef+ab)
            ans += tmp
            ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
