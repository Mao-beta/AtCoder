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
    Q = NI()
    D = deque()
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            x, c = X
            D.append([x, c])
        else:
            c = X[0]
            res = 0
            while c > 0:
                x, k = D.popleft()
                if c >= k:
                    c -= k
                    res += x * k
                else:
                    res += x * c
                    D.appendleft([x, k-c])
                    break
            print(res)


if __name__ == "__main__":
    main()
