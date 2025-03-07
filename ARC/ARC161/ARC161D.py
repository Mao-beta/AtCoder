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
    N, D = NMI()
    if D > (N-1)//2:
        print("No")
        return

    print("Yes")
    ans = []
    for d in range(1, D+1):
        for i in range(1, N+1):
            j = (i+d-1) % N + 1
            ans.append([i, j])

    for i, j in ans:
        print(i, j)


if __name__ == "__main__":
    main()
