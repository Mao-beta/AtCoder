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
    A.sort(reverse=True)
    ans = [0] * N
    S = set()
    for a in A:
        if a in S:
            ans[len(S)-1] += 1
        else:
            ans[len(S)] += 1

        S.add(a)

    for k in range(N):
        print(ans[k])


if __name__ == "__main__":
    main()