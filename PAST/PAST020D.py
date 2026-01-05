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
    C = [list(SI()) for _ in range(N)]
    A = "v<^>"
    ans = [["" for _ in range(N)] for _ in range(N)]
    for h in range(N):
        for w in range(N):
            c = C[h][w]
            c2 = A[(A.index(c)+1)%4]
            ans[w][N-1-h] = c2
    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
