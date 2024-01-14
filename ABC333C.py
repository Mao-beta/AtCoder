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
    N = NI()
    A = set()
    R = [1]
    for _ in range(30):
        R.append(R[-1]*10+1)
    for i in range(30):
        for j in range(30):
            for k in range(30):
                A.add(R[i]+R[j]+R[k])
    A = list(A)
    A.sort()
    print(A[N-1])


if __name__ == "__main__":
    main()
