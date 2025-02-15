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
    K = NI()
    # E[k]=[a, b]はkから始めたときの期待値が a*E[0]+b
    E = [[0, 0] for _ in range(K+1)]
    for k in range(K-1, -1, -1):
        E[k][1] = 1
        for i in range(1, 7):
            if k+i <= K:
                E[k][0] += E[k+i][0] / 6
                E[k][1] += E[k+i][1] / 6
            else:
                E[k][0] += 1/6
    a, b = E[0]
    print(b / (1-a))


if __name__ == "__main__":
    main()
