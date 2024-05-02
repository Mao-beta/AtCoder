import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    C = NLI() + NLI() + NLI()
    bingo = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
             [0, 3, 6], [1, 4, 7], [2, 5, 8],
             [0, 4, 8], [2, 4, 6]]
    ans = 0
    for P in permutations(range(9), 9):
        zannen = False
        P = list(P)
        for bs in bingo:
            order = [[P.index(b), b] for b in bs]
            order.sort()
            if C[order[0][1]] == C[order[1][1]] and C[order[0][1]] != C[order[2][1]]:
                zannen = True
        if not zannen:
            ans += 1
    print(ans / math.factorial(9))


if __name__ == "__main__":
    main()
