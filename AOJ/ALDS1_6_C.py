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


def partition(A, p, r):
    i = p
    x = A[r][1]
    for j in range(p, r):
        a = A[j][1]
        if a <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def main():
    N = NI()
    A = [SLI() for _ in range(N)]
    A = [[s, int(x)] for s, x in A]

    D = defaultdict(str)
    for s, x in A:
        D[x] += s

    quick_sort(A, 0, N-1)

    DD = defaultdict(str)
    for s, x in A:
        DD[x] += s

    is_stable = True
    for x in D.keys():
        if D[x] != DD[x]:
            is_stable = False

    print("Stable" if is_stable else "Not stable")
    for i in range(N):
        print(*A[i])


if __name__ == "__main__":
    main()
