import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    AB = EI(N)

    total = 0
    for a, b in AB:
        total += a

    def judge(X):
        # X秒後
        p = 0
        t = 0
        for a, b in AB:
            if t + a/b < X:
                t += a/b
                p += a
            else:
                p += (X - t) * b
                t += X - t
                break

        q = 0
        t = 0
        for a, b in AB[::-1]:
            if t + a / b < X:
                t += a / b
                q += a
            else:
                q += (X - t) * b
                t += X - t
                break

        # print(X, p, q, total)
        return p + q >= total

    ok = total
    ng = 0
    for _ in range(50):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    X = ok
    p = 0
    t = 0
    for a, b in AB:
        if t + a / b < X:
            t += a / b
            p += a
        else:
            p += (X - t) * b
            t += X - t
            break

    print(p)


if __name__ == "__main__":
    main()
