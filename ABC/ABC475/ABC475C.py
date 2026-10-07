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
    N, S, L = NMI()
    A = NLI()
    C = list(accumulate([0]+A))
    S -= 1
    ans = 0
    for l in range(N):
        for r in range(N):
            if l < S < r or r < S < l:
                x = abs(C[l] - C[S]) + abs(C[r] - C[l])
                if x <= L:
                    ans = max(ans, abs(r-l)+1)
                # print(l, S, r, x)
            else:
                if S <= l and S <= r:
                    x = max(C[l], C[r]) - C[S]
                    if x <= L:
                        ans = max(ans, abs(max(l, r) - S)+1)
                else:
                    x = C[S] - min(C[l], C[r])
                    if x <= L:
                        ans = max(ans, abs(S - min(l, r)) + 1)
    print(ans)

if __name__ == "__main__":
    main()
