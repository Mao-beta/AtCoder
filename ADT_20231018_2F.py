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
    N = NI()
    AB = EI(N)
    L = [0] * (N+1)
    R = [0] * (N+1)
    C = [0] * (N+1)
    for i, (a, b) in enumerate(AB):
        L[i+1] = L[i] + a / b
        C[i+1] = C[i] + a
    for i, (a, b) in enumerate(AB[::-1]):
        R[N-(i+1)] = R[N-i] + a / b

    for i in range(N):
        if abs(R[i] - L[i]) < 1e-5:
            print(C[i])
            return

        if (R[i]-L[i]) * (R[i+1]-L[i+1]) < 0:
            if R[i+1] > L[i]:
                ans = C[i] + (AB[i][0] + abs(R[i+1]-L[i]) * AB[i][1]) / 2
            else:
                ans = C[i] + (AB[i][0] - abs(R[i + 1] - L[i]) * AB[i][1]) / 2
            print(ans)
            return



if __name__ == "__main__":
    main()
