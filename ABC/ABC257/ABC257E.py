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
    C = [10**10] + NLI()
    D = {}
    for i in range(1, 10):
        D[C[i]] = i
    D = list(D.items())
    D.sort()
    # print(D)
    K = N // D[0][0]
    # K桁確定
    # print(K)
    ans = [D[0][1]] * K
    cost = D[0][0] * K

    for i in range(K):
        for d in range(9, D[0][1], -1):
            dc = C[d]
            gap = dc - D[0][0]
            # print(cost, gap)
            if cost + gap <= N:
                ans[i] = d
                cost += gap
                break

    print("".join(map(str, ans)))


if __name__ == "__main__":
    main()
