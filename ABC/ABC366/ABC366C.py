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
    Q = NI()
    C = Counter()
    ans = 0
    for _ in range(Q):
        t, *X = NMI()
        if t == 1:
            x = X[0]
            C[x] += 1
            if C[x] == 1:
                ans += 1
        elif t == 2:
            x = X[0]
            C[x] -= 1
            if C[x] == 0:
                ans -= 1
        else:
            print(ans)



if __name__ == "__main__":
    main()
