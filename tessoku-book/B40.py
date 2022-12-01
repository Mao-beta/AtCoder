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
    A = NLI()
    A = [a % 100 for a in A]
    C = Counter(A)
    ans = 0
    for i in range(100):
        if i == 0 or i == 50:
            ans += C[i] * (C[i]-1)
        else:
            ans += C[i] * C[100-i]
    print(ans // 2)


if __name__ == "__main__":
    main()
