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
    N, A, B = NMI()
    S = SI()
    CA = [0]
    CB = [0]
    for s in S:
        if s == "a":
            a = 1
            b = 0
        else:
            a = 0
            b = 1
        CA.append(CA[-1] + a)
        CB.append(CB[-1] + b)
    ans = 0
    for i in range(N):
        a = bisect.bisect_left(CA, CA[i]+A)
        b = bisect.bisect_left(CB, CB[i]+B)
        ans += max(0, b-a)
    print(ans)


if __name__ == "__main__":
    main()
