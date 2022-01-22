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
    S = NLI()
    ans = [0]

    def merge(A, l, mid, r):
        L = A[l:mid] + [10**20]
        R = A[mid:r] + [10**20]
        li = 0
        ri = 0
        for i in range(l, r):
            ans[0] += 1
            if L[li] <= R[ri]:
                A[i] = L[li]
                li += 1
            else:
                A[i] = R[ri]
                ri += 1


    def merge_sort(A, l, r):
        if r - l > 1:
            mid = (l+r) // 2
            merge_sort(A, l, mid)
            merge_sort(A, mid, r)
            merge(A, l, mid, r)

    merge_sort(S, 0, N)
    print(*S)
    print(ans[0])


if __name__ == "__main__":
    main()
