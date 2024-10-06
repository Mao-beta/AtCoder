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
    N, X = NMI()
    APBQ = EI(N)

    def judge(W):
        tmp = 0
        for a, p, b, q in APBQ:
            ttmp = 10**20
            if b*p-a*q >= 0:
                # 基本はT
                # Sを200個以下全探索
                for i in range(201):
                    x = p * i
                    n = a * i
                    if n >= W:
                        ttmp = min(ttmp, x)
                    else:
                        x += (W-n+b-1) // b * q
                        ttmp = min(ttmp, x)
            else:
                # 基本はS
                # Tを200個以下全探索
                for i in range(201):
                    x = q * i
                    n = b * i
                    if n >= W:
                        ttmp = min(ttmp, x)
                    else:
                        x += (W - n + a - 1) // a * p
                        ttmp = min(ttmp, x)
            tmp += ttmp
        # print(W, tmp)
        return tmp <= X

    ok = 0
    ng = 10**20
    while abs(ok - ng) > 1:
        W = (ok + ng) // 2
        if judge(W):
            ok = W
        else:
            ng = W

    print(ok)


if __name__ == "__main__":
    main()
