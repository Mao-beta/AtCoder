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
    V = NLI()
    INF = 1000
    ans = INF
    for a in range(1, 31):
        for b in range(a+1, 31):
            for c in range(b+1, 31):
                D = [INF] * 61
                D[0] = 0
                for i in range(31):
                    D[i + a] = min(D[i + a], D[i] + 1)
                    D[i + b] = min(D[i + b], D[i] + 1)
                    D[i + c] = min(D[i + c], D[i] + 1)
                tmp = 0
                for v in V:
                    tmp += D[v]
                ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
