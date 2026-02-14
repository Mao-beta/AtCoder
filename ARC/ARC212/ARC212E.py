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
    N = 5
    for P in permutations(range(1, N+1)):
        print(P)
        L = list(P)
        X = []
        ans = set()

        def rec():
            if len(X) == N-1:
                ans.add(tuple(X))
                return

            for i in range(len(L)-1):
                x = L[i]
                y = L[i+1]
                if x < y:
                    idx = i
                    v = x
                else:
                    idx = i+1
                    v = y
                L.pop(idx)
                X.append(v)
                rec()
                X.pop()
                L.insert(idx, v)

        rec()
        print(len(ans), ans)


if __name__ == "__main__":
    main()
