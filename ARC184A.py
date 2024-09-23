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
    N, M, Q = NMI()

    def diff(x, y):
        print("?", x+1, y+1, flush=True)
        return NI()

    def answer(ans):
        ans = [x+1 for x in ans]
        print("!", *ans, flush=True)

    all_zero_root = 0
    contain = []
    edges = [[] for _ in range(62)]
    for i in range(62):
        all_zero = True
        M = 16 if i < 61 else 24

        for j in range(1, M):
            x = i * 16
            y = x + j
            d = diff(x, y)
            edges[i].append([y, d])
            if d:
                all_zero = False
        if all_zero:
            all_zero_root = i
        else:
            contain.append(i)

    ans = []
    for i in contain:
        x = i * 16
        d = diff(i*16, all_zero_root*16)
        if d == 0:
            for y, dd in edges[i]:
                if dd:
                    ans.append(y)
        else:
            ans.append(x)
            for y, dd in edges[i]:
                if dd == 0:
                    ans.append(y)

    answer(ans)


if __name__ == "__main__":
    main()
