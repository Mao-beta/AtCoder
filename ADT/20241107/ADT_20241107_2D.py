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
    R, C = NMI()
    B = [list(SI()) for _ in range(R)]
    ans = [s[:] for s in B]
    for h in range(R):
        for w in range(C):
            for bh in range(R):
                for bw in range(C):
                    b = B[bh][bw]
                    if b == "." or b == "#":
                        continue
                    b = int(b)
                    if abs(h-bh) + abs(w-bw) <= b:
                        ans[h][w] = "."
    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
