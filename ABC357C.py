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
    C = [[["#"]]]
    N = NI()

    if N == 0:
        print("#")
        return

    def make(k):
        n = 3 ** k
        res = [["."]*n for _ in range(n)]
        B = C[k-1]
        for h in range(3):
            for w in range(3):
                if h == 1 and w == 1:
                    continue
                for hh in range(n//3):
                    for ww in range(n//3):
                        x = B[hh][ww]
                        res[h*n//3+hh][w*n//3+ww] = x
        return res

    for i in range(1, N+1):
        C.append(make(i))

    for row in C[-1]:
        print("".join(row))


if __name__ == "__main__":
    main()
