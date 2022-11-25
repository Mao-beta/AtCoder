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
    N = NI()
    A = NLI()
    B = NLI()[::-1]

    target = 0
    for i in range(N):
        if A[i] == B[i]:
            target = A[i]

    if target == 0:
        print("Yes")
        print(*B)
        exit()

    rem = set()
    T = set()
    for i in range(N):
        a, b = A[i], B[i]
        if a == b == target:
            T.add(i)
        elif A[i] == target or B[i] == target:
            continue
        else:
            rem.add(i)

    if len(rem) >= len(T):
        print("Yes")
        for r, t in zip(rem, T):
            B[r], B[t] = B[t], B[r]
        print(*B)

    else:
        print("No")


if __name__ == "__main__":
    main()
