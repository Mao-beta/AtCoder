import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    Q = NI()
    S = deque()
    S.append(1)
    ans = 1
    P = [1]
    for _ in range(Q+5):
        P.append(P[-1] * 10 % MOD99)

    for _ in range(Q):
        q, x, *_ = NLI() * 2
        if q == 1:
            S.append(x)
            ans = (ans * 10 + x) % MOD99
        elif q == 2:
            d = S.popleft()
            ans = (ans - d * P[len(S)]) % MOD99
        else:
            print(ans)


if __name__ == "__main__":
    main()
