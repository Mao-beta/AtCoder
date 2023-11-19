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
    N, Q = NMI()
    C = NLI()
    S = [set()] + [{c} for c in C]
    # queryでxと言われたときに実際に見る箱
    Labels = list(range(N+1))
    for qi in range(Q):
        a, b = NMI()
        la, lb = Labels[a], Labels[b]
        Sa, Sb = S[la], S[lb]

        if len(Sa) <= len(Sb):
            for c in S[la]:
                Sb.add(c)
            S[la] = set()
            print(len(S[lb]))

        else:
            for c in S[lb]:
                Sa.add(c)
            S[lb] = set()
            print(len(S[la]))
            Labels[a], Labels[b] = Labels[b], Labels[a]


if __name__ == "__main__":
    main()
