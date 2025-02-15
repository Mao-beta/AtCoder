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
    D = [0] * 401
    for i in range(400):
        if (i+2015) % 400 == 0:
            D[i+1] = (D[i] + 2) % 7
        elif (i+2015) % 100 == 0:
            D[i+1] = (D[i] + 1) % 7
        elif (i+2015) % 4 == 0:
            D[i+1] = (D[i] + 2) % 7
        else:
            D[i+1] = (D[i] + 1) % 7
    m = D[:400].count(0)
    ans = 0
    k, r = divmod(N-2014, 400)
    ans += k * m
    ans += D[1:r+1].count(0)
    print(ans)


if __name__ == "__main__":
    main()
