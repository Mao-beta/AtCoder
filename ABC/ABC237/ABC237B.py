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


def transpose(A):
    """
    2次元list Aの転置行列
    """
    return [list(x) for x in zip(*A)]

def main():
    H, W = NMI()
    A = [NLI() for _ in range(H)]
    A = transpose(A)
    for i in range(W):
        print(*A[i])


if __name__ == "__main__":
    main()
