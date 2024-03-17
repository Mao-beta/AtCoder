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
    W = NI()
    H = NI()
    N = NI()
    S = set()
    K = set()
    for _ in range(N):
        s, k = NMI()
        S.add(s)
        K.add(k)
    ans = H * W - (W - len(S)) * (H - len(K)) - N
    print(ans)


if __name__ == "__main__":
    main()
