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
    N = NI()
    A = NLI()
    X = [[] for _ in range(10**6+1)]
    ans = 10**6
    for i, a in enumerate(A):
        X[a].append(i)
        if len(X[a]) >= 2:
            ans = min(ans, X[a][-1] - X[a][-2] + 1)
    print(ans if ans != 10**6 else -1)


if __name__ == "__main__":
    main()
