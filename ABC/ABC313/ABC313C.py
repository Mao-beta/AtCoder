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
    A = NLI()

    if max(A) - min(A) <= 1:
        print(0)
        exit()

    A.sort()
    t, r = divmod(sum(A), N)

    # print(t, r)
    # tがN-r個、t+1がr個
    ans = 0
    for i, a in enumerate(A):
        if i < N-r:
            ans += abs(t-a)
        else:
            ans += abs(t+1-a)

    print(ans // 2)


if __name__ == "__main__":
    main()
