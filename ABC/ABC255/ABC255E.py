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


def main():
    N, M = NMI()
    S = NLI()
    X = set(NLI())

    odds = Counter() # -a + key
    evens = Counter() # a + key

    A = [0] * N

    evens[0] += 1
    prev = 0
    A[0] = 0
    for i in range(0, N, 2):
        if i >= N-2:
            continue
        a, b = S[i], S[i+1]
        prev = prev - a + b
        evens[prev] += 1
        A[i+2] = prev

    odds[S[0]] += 1
    prev = S[0]
    A[1] = S[0]
    for i in range(1, N, 2):
        if i >= N-2:
            continue
        a, b = S[i], S[i+1]
        prev = prev - a + b
        odds[prev] += 1
        A[i+2] = prev

    ans = 0
    for i in range(N):
        for x in X:
            tmp = 0

            # A[i]がxのとき
            if i % 2 == 0:
                a0 = x - A[i]
                for y in X:
                    tmp += evens[y - a0]
                    tmp += odds[y + a0]

            else:
                a0 = A[i] - x
                for y in X:
                    tmp += evens[y - a0]
                    tmp += odds[y + a0]

            ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
