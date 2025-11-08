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
    N, K = NMI()
    S = SI()
    C = Counter()
    for i in range(N-K+1):
        T = S[i:i+K]
        C[T] += 1
    R = C.most_common()
    R.sort(key=lambda c: (-c[1], c[0]))
    x = R[0][1]
    print(x)
    for c, k in R:
        if k == x:
            print(c, end=' ')


if __name__ == "__main__":
    main()
