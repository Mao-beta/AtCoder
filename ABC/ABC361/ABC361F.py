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
    S = {1}
    R = {i**2: i for i in range(1, 10**3+1)}
    V = {1}
    for a in range(2, 10**6+1):
        for b in range(3, 63):
            x = a ** b
            if x > N:
                break
            V.add(x)
            if b % 2 == 0:
                S.add(x)
            if a in R:
                S.add(x)

    ans = len(V) + math.isqrt(N) - len(S)
    print(ans)


if __name__ == "__main__":
    main()
