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
    N, K = NMI()
    S = SI()
    P = set(permutations(S))
    ans = 0
    for T in P:
        ok = True
        for l in range(N-K+1):
            rev = True
            for i in range(K):
                if T[l+i] != T[l+K-1-i]:
                    rev = False
                    break
            if rev:
                ok = False
                break
        if ok:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
