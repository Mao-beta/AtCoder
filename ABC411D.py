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
    N, Q = NMI()
    S = [[] for _ in range(N+1)]
    for t in range(Q):
        q, *X = SMI()
        if q == "1":
            x = int(X[0])
            S[x].append([t, 0])
        elif q == "2":
            p, s = X
            p = int(p)
            S[p].append([t, s[::-1]])
        else:
            x = int(X[0])
            S[0].append([t, x])
    i = 0
    ans = []
    T = Q
    while S[i]:
        t, x = S[i].pop()
        if t > T:
            continue
        if isinstance(x, int):
            i = x
        else:
            ans.append(x)
        T = t
    print("".join(ans)[::-1])


if __name__ == "__main__":
    main()
