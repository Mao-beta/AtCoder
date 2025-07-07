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
    N, M = NMI()
    A = NLI()
    B = NLI()

    def f(_A, _B):
        now = 0
        res = []
        for i, a in enumerate(_A):
            if a == _B[now]:
                now += 1
                res.append(i)
            if now == len(_B):
                break
        return res

    X = f(A, B)
    Y = f(A[::-1], B[::-1])
    Y = [N-1-y for y in Y[::-1]]
    # print(X, Y)
    if len(X) == len(Y) == M and X != Y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
