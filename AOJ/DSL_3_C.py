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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, Q = NMI()
    A = NLI()
    X = NLI()

    for x in X:
        D = deque()
        total = 0
        ans = 0
        for a in A:
            D.append(a)
            total += a
            while D and total > x:
                total -= D[0]
                D.popleft()
            l = len(D)
            ans += l
        print(ans)


if __name__ == "__main__":
    main()
