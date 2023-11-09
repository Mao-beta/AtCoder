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
    N, M = NMI()
    S = [0] * M
    for i in range(M):
        c = NI()
        A = NLI()
        for a in A:
            a -= 1
            S[i] |= 1 << a

    ok = (1 << N) - 1
    ans = 0
    for k in range(1, M+1):
        for C in combinations(S, r=k):
            tmp = 0
            for x in C:
                tmp |= x
            if tmp == ok:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
