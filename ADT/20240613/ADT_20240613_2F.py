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
    S = NLI()
    T = NLI()
    hq = []
    INF = 10**20
    ans = [INF] * N
    for i, t in enumerate(T):
        heappush(hq, [t, i])
    while hq:
        t, i = heappop(hq)
        if ans[i] <= t:
            continue
        ans[i] = t
        heappush(hq, [t+S[i], (i+1)%N])
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
