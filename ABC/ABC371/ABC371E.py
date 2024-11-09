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
    L = [0] * (N+1)
    X = []
    S = set(A)
    for i, a in enumerate(A):
        X.append(i-L[a]+1)
        L[a] = i+1
    for s in S:
        X.append(N-L[s]+1)
    ans = len(S) * (N+1) * N // 2
    for x in X:
        ans -= x * (x-1) // 2
    print(ans)


if __name__ == "__main__":
    main()
