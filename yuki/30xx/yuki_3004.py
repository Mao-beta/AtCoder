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


def main():
    K = NI()
    LM = EI(K)
    N = sum(l * m for l, m in LM)
    D = defaultdict(list)
    for l, m in LM:
        D[l].append(m)
        D[m].append(1)
    ans = 1
    fac = 1
    for i in range(1, N+1):
        fac = fac * i % MOD99
        ans = ans * i % MOD99
        # print(i, fac)
        for k in D[i]:
            ans = ans * pow(pow(fac, k, MOD99), MOD99-2, MOD99) % MOD99
    print(ans)


if __name__ == "__main__":
    main()
