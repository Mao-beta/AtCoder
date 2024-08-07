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
    for b in range(30):
        X = [(a >> b) & 1 for a in A]

        Y = []
        y = 0
        for x in X:
            y ^= x
            Y.append(y)
        C = [Y.count(0), Y.count(1)]
        tmp = 0

        rev = 0
        for x in Y:
            tmp += C[1]
            C[x^rev] -= 1
            if x^rev:
                rev ^= 1
                C = C[::-1]

        ans += tmp << b

    print(ans - sum(A))


if __name__ == "__main__":
    main()
