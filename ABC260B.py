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
    N, X, Y, Z = NMI()
    A = NLI()
    B = NLI()
    T = [(a+b, i) for i, (a, b) in enumerate(zip(A, B))]
    ok = set()
    A = [(a, i) for i, a in enumerate(A)]
    A.sort(key=lambda x: (-x[0], x[1]))
    for i in range(X):
        ok.add(A[i][1])

    B = [(b, i) for i, b in enumerate(B)]
    B.sort(key=lambda x: (-x[0], x[1]))

    for b, i in B:
        if len(ok) == X+Y:
            break
        if i not in ok:
            ok.add(i)

    T.sort(key=lambda x: (-x[0], x[1]))

    for t, i in T:
        if len(ok) == X + Y + Z:
            break
        if i not in ok:
            ok.add(i)

    ans = sorted(list(ok))
    for a in ans:
        print(a+1)


if __name__ == "__main__":
    main()
