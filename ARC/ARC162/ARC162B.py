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
    P = NLI()
    ans = []
    for i in range(N-1):
        if P[i] == i+1:
            continue
        if P[-1] == i+1:
            P = P[:i] + P[-2:] + P[i:-2]
            ans.append([N-1, i])
            # print(P)
        idx = P.index(i+1)
        if idx+1 <= N-1:
            P = P[:i] + P[idx:idx+2] + P[i:idx] + P[idx+2:]
            ans.append([idx+1, i])
            # print(P, ans, i, idx)
    if P[-1] == N:
        print("Yes")
        print(len(ans))
        for i, j in ans:
            print(i, j)
    else:
        print("No")


if __name__ == "__main__":
    main()
