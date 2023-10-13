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

from typing import List, Tuple
def maximum_independent_set(N: int, G: List[List[int]]) -> Tuple[int, List[int]]:
    """
    無向グラフにおける最大独立集合のサイズと点のリストを求める(N<=40)
    :param N: 頂点数
    :param G: 隣接リスト(0-index)
    :return: 最大独立集合のサイズ、点のリスト
    """
    # 半分全列挙
    Nf = N // 2
    Nl = N - Nf

    # 前半のなかで独立集合か？
    is_ind_f = [0] * (1 << Nf)
    popcnt_f = [0] * (1 << Nf)
    for case in range(1 << Nf):
        # caseは独立集合かを確認
        ng = False
        cnt = 0  # popcount
        for i in range(Nf):
            if (case >> i) & 1:
                cnt += 1
                for j in G[i]:
                    if j < Nf and (case >> j) & 1:
                        ng = True
                        break
                if ng:
                    break
        if not ng:
            is_ind_f[case] = 1
        popcnt_f[case] = cnt

    # 後半のなかで独立集合か？
    is_ind_l = [0] * (1 << Nl)
    popcnt_l = [0] * (1 << Nl)
    for case in range(1 << Nl):
        # caseは独立集合かを確認
        ng = False
        cnt = 0  # popcount
        for i in range(Nl):
            if (case >> i) & 1:
                cnt += 1
                for j in G[Nf + i]:
                    if j >= Nf and (case >> (j - Nf)) & 1:
                        ng = True
                        break
                if ng:
                    break
        if not ng:
            is_ind_l[case] = 1
        popcnt_l[case] = cnt

    # 前半をbitDP
    # dp[S]: Sの部分集合での最大独立集合
    dp = [0] * (1 << Nf)
    for i in range(Nf):
        dp[1 << i] = 1
    for case in range(1, 1 << Nf):
        for i in range(Nf):
            if (case >> i) & 1:
                continue
            nc = case | (1 << i)
            if is_ind_f[nc]:
                dp[nc] = max(dp[nc], dp[case] + 1)
            else:
                dp[nc] = max(dp[nc], dp[case])

    # 後半を全探索
    ans = 0
    ans_former = 0
    ans_case = 0
    for case in range(1 << Nl):
        # caseは独立集合かを確認
        if not is_ind_l[case]:
            continue
        # formersはcaseから繋がってない前半の頂点の集合
        formers = (1 << Nf) - 1
        for i in range(Nl):
            if (case >> i) & 1:
                for j in G[Nf + i]:
                    if j < Nf:
                        formers &= ~(1 << j)

        if dp[formers] + popcnt_l[case] > ans:
            ans = dp[formers] + popcnt_l[case]
            ans_case = case
            ans_former = formers

    # 復元
    # ans_formerの下位集合のうち、独立集合で、かつdpの値が等しいものを取ってくる
    now = ans_former
    ans_just = ans_former
    while now > 0:
        if is_ind_f[now] and dp[now] == dp[ans_former]:
            ans_just = now
        now = (now-1) & ans_former

    ans_set = []
    for i in range(N):
        if i < Nf:
            if (ans_just >> i) & 1:
                ans_set.append(i)
        else:
            if (ans_case >> (i-Nf)) & 1:
                ans_set.append(i)

    return ans, ans_set

def main():
    N, M = NMI()
    AB = EI(M)
    AB = [[x-1, y-1] for x, y in AB]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)

    x, P = maximum_independent_set(N, G)
    print(x)


if __name__ == "__main__":
    main()
