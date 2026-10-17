import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        AI = [[a, i] for i, a in enumerate(A)]
        AI.sort()
        B = NLI()
        k = 0
        total = sum(A)
        best = total
        best_k = 0
        for n in range(N):
            total += B[n] - AI[n][0]
            if total > best:
                best = total
                best_k = n+1
        ans = ["0"] * N
        for k in range(best_k):
            ans[AI[k][1]] = "1"
        print("".join(ans))


if __name__ == "__main__":
    main()
