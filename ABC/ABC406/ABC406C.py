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
    P = NLI()
    l = 0
    r = 0
    while l < N - 1 and P[l] > P[l + 1]:
        l += 1
    r = l
    while r < N-1 and P[r] < P[r+1]:
        r += 1
    while r < N-1 and P[r] > P[r+1]:
        r += 1
    if r == N-1:
        print(0)
        return
    ans = 0
    while r < N-1:
        bl, br = l, r
        while l < N - 1 and P[l] > P[l + 1]:
            l += 1
        while r < N - 1 and P[r] > P[r + 1]:
            r += 1
        # ans += (l-bl) * (r-br)
        # print(l, bl, r, br)
        if r == N-1:
            break
        bl, br = l, r
        while l < N - 1 and P[l] < P[l + 1]:
            l += 1
        while r < N - 1 and P[r] < P[r + 1]:
            r += 1
        ans += (l - bl) * (r - br)
        # print(l, bl, r, br)
        if r == N - 1:
            break
    print(ans)


if __name__ == "__main__":
    main()
