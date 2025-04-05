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


def main(N, A, B, C):
    oneone = []
    zeroone = []
    onezero = []
    base = 0
    for i in range(N):
        a, b, c = A[i], B[i], C[i]
        if a == 1:
            base += c
        if a == 1 and b == 1:
            oneone.append(c)
        elif a == 0 and b == 1:
            zeroone.append(c)
        elif a == 1 and b == 0:
            onezero.append(c)
    oneone.sort(reverse=True)
    zeroone.sort()
    onezero.sort(reverse=True)


    def judge(X):
        # 1->1のものをX個追加で反転
        res = 0
        OZ = oneone[:X] + onezero
        ZO = oneone[:X] + zeroone
        OZ.sort(reverse=True)
        ZO.sort()
        now = base
        for x in OZ:
            now -= x
            res += now
        for x in ZO:
            now += x
            res += now

        res2 = 0
        OZ = oneone[:X+1] + onezero
        ZO = oneone[:X+1] + zeroone
        OZ.sort(reverse=True)
        ZO.sort()
        now = base
        for x in OZ:
            now -= x
            res2 += now
        for x in ZO:
            now += x
            res2 += now
        return res <= res2

    ok = N+1
    ng = -1
    # print(ok)
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        # print(X)
        if judge(X):
            ok = X
        else:
            ng = X

    ans = 10**18
    for X in range(ok-3, ok+4):
        if X < 0:
            continue
        res = 0
        OZ = oneone[:X] + onezero
        ZO = oneone[:X] + zeroone
        OZ.sort(reverse=True)
        ZO.sort()
        now = base
        for x in OZ:
            now -= x
            res += now
        for x in ZO:
            now += x
            res += now
        # print(X, res)
        ans = min(ans, res)
    return ans


if __name__ == "__main__":
    N = NI()
    A = NLI()
    B = NLI()
    C = NLI()
    ans = main(N, A, B, C)
    print(ans)