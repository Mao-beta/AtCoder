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


import random
def rabin_karp(s, t):
    """
    ローリングハッシュ
    ハッシュ化にO(|S|+|T|)、検索にO(|S|)
    sの連続部分文字列でtに一致するものの始点のindexをまとめてlistで返す
    """
    def exe(x, m):
        th = 0
        for c in tt:
            th = (th * x + c) % m

        sh = 0
        for c in st[:l]:
            sh = (sh * x + c) % m
        xl = pow(x, l - 1, m)

        matched = set()
        if sh == th:
            matched.add(0)
        for i, (c0, c1) in enumerate(zip(st, st[l:]), start=1):
            sh = ((sh - c0 * xl) * x + c1) % m
            if sh == th:
                matched.add(i)

        return matched

    l = len(t)
    st = list(map(ord, s))
    tt = list(map(ord, t))
    # Xはなるべくst,ttの最大要素より大きくする
    # Mはとりあえず2^61-1(素数)を設定する
    xs = random.sample(range(10 ** 9, 10 ** 10), 3)
    ans = exe(xs[0], 2305843009213693951)
    ans.intersection_update(exe(xs[1], 2305843009213693951))
    ans.intersection_update(exe(xs[2], 2305843009213693951))
    return sorted(ans)


def main():
    N = NI()
    S = SI()
    T = SI()

    D = {"R": 0, "G": 1, "B": 2}
    S = [D[s] for s in S]
    T = [D[t] for t in T]
    # print(S)

    def make_hash(L, b, m):
        res = [0]
        for l in L:
            res.append((res[-1]*b + l) % m)
        return res

    def sub_hash(H, P, M, l, r):
        # 部分文字列S[l:r]のhashを計算する
        return (H[r] - P[r-l] * H[l]) % M

    # M = (1<<61) - 1
    M = MOD99
    ans = 0
    powB = [1] * (N+1)

    TT = [0] * N

    for target in range(3):
        for i in range(N):
            TT[i] = (target - T[i]) % 3
        # print(TT)

        Ks = set()

        B3 = random.sample(range(10 ** 4, 10 ** 5), 2)

        for bi, B in enumerate(B3):
            for i in range(1, N+1):
                powB[i] = powB[i-1] * B % M

            HS = make_hash(S, B, M)
            HT = make_hash(TT, B, M)
            # print(HS)
            # print(HT)

            sub_ans = set()
            for k in range(-N+1, N):
                if k < 0:
                    hs = sub_hash(HS, powB, M, -k, N)
                    ht = sub_hash(HT, powB, M, 0, N+k)
                else:
                    hs = sub_hash(HS, powB, M, 0, N-k)
                    ht = sub_hash(HT, powB, M, k, N)

                if hs == ht:
                    sub_ans.add(k)

            # print(bi, Ks, sub_ans)
            if bi == 0:
                Ks |= sub_ans
                # print(Ks, 0)
            else:
                Ks.intersection_update(sub_ans)
                # print(Ks)

        # print(Ks)
        ans += len(Ks)

    print(ans)


if __name__ == "__main__":
    main()
