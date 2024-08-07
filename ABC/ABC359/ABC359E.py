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
    N = NI()
    H = NLI()
    D = deque()
    INF = 10**10
    D.append([INF, 0])
    s = 0
    for i, h in enumerate(H, start=1):
        while D and D[-1][0] < h:
            hl, xl = D.pop()
            s -= (xl - D[-1][1]) * hl
        s += h * (i - D[-1][1])
        D.append([h, i])
        # print(D)

        print(s+1, end=" ")



if __name__ == "__main__":
    main()
