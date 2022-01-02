import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(100000)
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
    A = NI()
    B = NI()
    C = NI()
    X = NI()
    ans = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if X == a * 500 + b * 100 + c * 50:
                    ans += 1
    print(ans)



if __name__ == "__main__":
    main()
