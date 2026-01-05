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
    D = dict()
    for _ in range(N):
        a, b, c = NMI()
        D[(a, b)] = c
        D[(b, a)] = c
    X = NLI()
    ans = X[0]
    for x in X[1:]:
        if (ans, x) in D:
            ans = D[(ans, x)]
        else:
            ans += x
    print(ans)


if __name__ == "__main__":
    main()
