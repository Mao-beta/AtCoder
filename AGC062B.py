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
    N, K = NMI()
    C = NLI()
    P = NLI()
    PI = [(a, i) for i, a in enumerate(P)]
    PI.sort()
    cnt = 0
    now = 0
    for idx in range(N-1):
        if PI[idx][1] > PI[idx+1][1]:
            cnt += 1

    if cnt > K:
        print(-1)
        return

    print(PI)
    print(cnt, K)


if __name__ == "__main__":
    main()
