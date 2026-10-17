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
    l1, l2, l3 = NMI()
    RBY = NLI()
    L = [l1+l2, l1+l3, l2+l3]
    ans = 10 ** 18
    for P in permutations(RBY):
        tmp = 0
        for l, x in zip(L, P):
            tmp += l * x * 2
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
