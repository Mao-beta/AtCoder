import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def main(N, K):
    Deq = defaultdict(int)
    Dle = defaultdict(int)
    Dgr_e = defaultdict(int)
    Dgr_l = defaultdict(int)
    zero = 1

    for i, s in enumerate(str(N)):
        s = int(s)
        Deq2 = defaultdict(int)
        Dle2 = defaultdict(int)
        Dgr_e2 = defaultdict(int)
        Dgr_l2 = defaultdict(int)
        zero2 = 0

        if i == 0:
            for x in range(s+1):
                if x > K:
                    if x == s:
                        Dgr_e2[x] += zero
                    else:
                        Dgr_l2[x] += zero
                elif x == s:
                    Deq2[x] += zero
                elif x > 0:
                    Dle2[x] += zero
                else:
                    zero2 += zero
        else:
            for x in range(10):
                if x > K:
                    Dgr_l2[x] += zero
                elif x > 0:
                    Dle2[x] += zero
                else:
                    zero2 += zero

        for key, val in Deq.items():
            for x in range(s):
                if key * x <= K:
                    Dle2[key * x] += val
                else:
                    Dgr_l2[key * x] += val

            if key * s <= K:
                Deq2[key * s] += val
            else:
                Dgr_e2[key * s] += val

        for key, val in Dgr_l.items():
            for x in range(10):
                if key * x <= K:
                    Dle2[key * x] += val
                else:
                    Dgr_l2[key * x] += val

        for key, val in Dgr_e.items():
            for x in range(s):
                if key * x <= K:
                    Dle2[key * x] += val
                else:
                    Dgr_l2[key * x] += val

            if key * s <= K:
                Deq2[key * s] += val
            else:
                Dgr_e2[key * s] += val

        for key, val in Dle.items():
            for x in range(10):
                if key * x <= K:
                    Dle2[key * x] += val
                else:
                    Dgr_l2[key * x] += val

        Deq = Deq2
        Dle = Dle2
        Dgr_e = Dgr_e2
        Dgr_l = Dgr_l2
        zero = zero2

        # print(N, K, i, s)
        # print(Deq)
        # print(Dle)
        # print(Dgr_e)
        # print(Dgr_l)

    ans = sum(Deq.values()) + sum(Dle.values())
    # print(Deq)
    # print(Dle)
    # print(ans)
    # print(Deq, Dle, zero)
    return ans


def guchoku(N, K):
    ans = [0] * (K+1)
    for i in range(1, N+1):
        tmp = 1
        for x in str(i):
            tmp *= int(x)
        if tmp <= K:
            ans[tmp] += 1

    # print(ans)
    return sum(ans)


if __name__ == "__main__":
    N, K = NMI()
    print(main(N, K))
    exit()
    for N in range(1, 10000000):
        for K in range(1, 2):
            ans = main(N, K)
            gu = guchoku(N, K)
            # print(N, K, ans, gu)
            assert ans == gu, f"{N}, {K}, {ans}, {gu}"
