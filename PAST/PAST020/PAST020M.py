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
    A = sorted(NLI())

    def judge(X):
        # X以下のものがN(N-1)/2個以上あるか？
        res = 0
        r = N
        for i, a in enumerate(A):
            while r > 0:
                b = A[r-1]
                x = int(str(a) + str(b))
                if x > X:
                    r -= 1
                else:
                    break
            if i < r:
                res += r-1
            else:
                res += r

        return res >= N*(N-1)//2

    ok = 10**20
    ng = 0
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
