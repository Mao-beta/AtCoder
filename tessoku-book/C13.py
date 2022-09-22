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
    N, P = NMI()
    A = NLI()
    A = [a % MOD for a in A]
    C = Counter(A)

    if P == 0:
        z = C[0]
        print(z*(z-1)//2 + z * (N-z))
        exit()

    ans = 0
    for a, k in C.items():
        b = P * pow(a, MOD-2, MOD) % MOD
        if a != b:
            ans += k * C[b]
        else:
            ans += k * (k-1)

    print(ans // 2)


if __name__ == "__main__":
    main()
