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
    if A[0] != 0:
        print(0)
        exit()
    C = Counter(A)
    if C[0] > 1:
        print(0)
        exit()

    ans = 1
    M = max(A)
    for i in range(1, M+1):
        if C[i] == 0:
            print(0)
            exit()

        now = C[i]
        prev = C[i-1]

        ans = ans * pow((pow(2, prev, MOD) - 1), now, MOD) % MOD
        ans = ans * pow(2, now*(now-1)//2, MOD) % MOD

    print(ans)


if __name__ == "__main__":
    main()
