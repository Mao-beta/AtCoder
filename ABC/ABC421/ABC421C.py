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
    S = SI()
    Bs = [i for i in range(2*N) if S[i] == "B"]
    evens = list(range(0, 2*N, 2))
    odds = list(range(1, 2*N, 2))
    ans = 10**20
    tmp = 0
    for b, x in zip(Bs, evens):
        tmp += abs(b-x)
    ans = min(ans, tmp)
    tmp = 0
    for b, x in zip(Bs, odds):
        tmp += abs(b - x)
    ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
