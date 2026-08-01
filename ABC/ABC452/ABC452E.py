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
    N, M = NMI()
    A = [0] + NLI()
    B = [0] + NLI()
    CA = list(accumulate([0] + A))
    XA = [i*a for i, a in enumerate(A)]
    CXA = list(accumulate([0]+XA))
    ans = 0
    for j, b in enumerate(B):
        if j <= 1:
            continue
        tmp = CXA[-1]
        for l in range(0, N+1, j):
            r = l + j
            r = min(r, N+1)
            # print(CA)
            # print(j, b, l, r, CA[r], CA[l])
            tmp -= l * (CA[r]-CA[l])
        # print(tmp)
        ans += tmp * b
        ans %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
