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
    N, Q = NMI()
    HT = [SMI() for _ in range(Q)]
    # num, l, r, next_idx
    hq = [[0, 0, 1, 0]]
    while hq:
        num, l, r, idx = heappop(hq)
        if idx == N:
            print(num)
            exit()

        h, t = HT[idx]
        t = int(t) - 1
        if h == "L":
            if l < r:
                if r < t:
                    tx = t - N
                else:
                    tx = t
                if r != t:
                    heappush(hq, [num+abs(tx-l), t, r, idx+1])

        else:
            now = r
            opposed = l




if __name__ == "__main__":
    main()
