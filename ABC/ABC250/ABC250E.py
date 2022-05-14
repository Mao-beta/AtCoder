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


def main():
    N = NI()
    A = NLI()
    B = NLI()
    Q = NI()
    XY = [NLI() for i in range(Q)]

    # i個見たときの種類数
    CA = [0] * (N+1)
    CB = [0] * (N+1)
    # i個目までの集合
    SA = set()
    SB = set()
    # SA/SBに初めて追加する値のリスト
    KA = []
    KB = []

    for i, a in enumerate(A):
        if a not in SA:
            SA.add(a)
            KA.append(a)
            CA[i+1] = CA[i] + 1
        else:
            CA[i+1] = CA[i]

    for i, b in enumerate(B):
        if b not in SB:
            SB.add(b)
            KB.append(b)
            CB[i+1] = CB[i] + 1
        else:
            CB[i+1] = CB[i]

    # 種類数がともにkのとき、AとBのどちらかにのみ含まれている値の集合
    S = set()
    k_ans = [0]
    for ka, kb in zip(KA, KB):
        if ka in S:
            S.discard(ka)
        else:
            S.add(ka)

        if kb in S:
            S.discard(kb)
        else:
            S.add(kb)

        if len(S) == 0:
            k_ans.append(1)
        else:
            k_ans.append(0)


    for x, y, i in XY:
        if CA[x] == CB[y] and k_ans[CA[x]]:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
