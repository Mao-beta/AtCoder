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


def main(N, S):
    ans = 0
    endA = 0
    startB = 0
    both = 0
    for s in S:
        if "AB" in s:
            ans += s.count("AB")
        if s[0] == "B" and s[-1] == "A":
            both += 1
        elif s[0] == "B":
            startB += 1
        elif s[-1] == "A":
            endA += 1

    if endA > 0 or startB > 0:
        ans += both
        ans += min(endA, startB)
    elif both > 1:
        ans += both - 1

    return ans


def guchoku(N, S):
    ans = 0
    for P in permutations(S):
        ans = max(ans, "".join(P).count("AB"))
    return ans


if __name__ == "__main__":
    N = NI()
    S = [SI() for _ in range(N)]
    print(main(N, S))


    # from random import randint
    #
    # N = 7
    # W = ["A", "B", "BA", "AB"]
    #
    # for _ in range(100):
    #     S = [W[randint(0, 3)] for _ in range(N)]
    #
    #     ans = main(N, S)
    #     g = guchoku(N, S)
    #     print(N, S)
    #     print(ans, g)
    #     assert ans == g