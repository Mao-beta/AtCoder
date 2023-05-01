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
    N, M = NMI()
    A = NLI()
    B = [0] * (N+1)
    for a in A:
        B[a] = 1

    ans = []

    D = deque()
    for i in range(1, N+1):
        if B[i]:
            D.append(i)
        else:
            ans.append(i)
            while D:
                x = D.pop()
                ans.append(x)

    print(*ans)


if __name__ == "__main__":
    main()
