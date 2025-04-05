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
    LR = EI(N)
    X = [0] * (10**6+10)
    X[1] = 1
    X[5*10**5+1] = -1
    for l, r in LR:
        X[l] -= 1
        X[r+1] += 1
        X[l+1] += 1
        X[r+2] -= 1
    X = list(accumulate(X))
    print(X[:10])
    X = list(accumulate(X))
    print(X[:10])
    Q = NI()
    Xs = [[NI(), i] for i in range(Q)]
    ans = [0] * Q
    Xs.sort()
    print(X[:10])


if __name__ == "__main__":
    main()
