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
    S = list(SI())

    def check(l):
        if l < 0 or l+3 > N:
            return False
        return "".join(S[l:l+3]) == "ABC"

    ans = sum(check(l) for l in range(N+1-3))
    for _ in range(Q):
        x, c = SMI()
        x = int(x) - 1
        for l in range(x-2, x-2+5):
            ans -= check(l)
        S[x] = c
        for l in range(x-2, x-2+5):
            ans += check(l)
        print(ans)


if __name__ == "__main__":
    main()
