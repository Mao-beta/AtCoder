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
    A = NLI()
    ans = 0
    for l in range(1, N+1):
        for r in range(l, N+1):
            s = sum(A[l-1:r])
            ok = True
            for i in range(l, r+1):
                a = A[i-1]
                if s % a == 0:
                    ok = False
            # print(l, r, A[l-1:r], s, ok)
            if ok:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
