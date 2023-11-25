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


def solve(N, K, P, A):
    res = "Bob"

    P = [0, 0] + P
    A = [0] + A
    G = [[] for _ in range(N+1)]
    for i in range(2, N+1):
        G[P[i]].append(i)

    S = [set() for _ in range(N+1)]
    # i以下の-1の数
    M = [0] * (N+1)

    def dfs(now):
        if A[now] == -1:
            M[now] += 1
        for g in G[now]:
            dfs(g)
            M[now] += M[g]
        if P[now] > 0:
            S[P[now]] |= S[now] | {A[now]}


    def short(i):
        res = set()
        for k in range(K):
            if k not in S[i]:
                res.add(k)
        return res

    dfs(1)
    # print(M)

    for i in range(1, N+1):
        # -1が2個以上ある部分木は次でつぶされるのでだめ
        if M[i] > 1:
            continue
        # 見てる点がKならだめ
        if A[i] == K:
            continue
        # 部分木にKがあってもだめ
        if K in S[i]:
            continue

        # K未満を揃えるのにたりない要素
        rem = short(i)

        # K未満がすでに全部ある
        if len(rem) == 0:
            res = "Alice"
            break
        # K未満は1個だけ足りないが-1が1個だけある
        if len(rem) == 1 and M[i] == 1:
            res = "Alice"
            break
        # K未満は1個だけ足りないがA[i]がそれ
        if len(rem) == 1 and A[i] in rem:
            res = "Alice"
            break
        # K未満は2個だけ足りないがA[i]がそのどちらかで-1が1個ある
        if len(rem) == 2 and M[i] == 1 and A[i] in rem:
            res = "Alice"
            break

    return res


def main():
    T = NI()
    for _ in range(T):
        N, K = NMI()
        P = NLI()
        A = NLI()
        res = solve(N, K, P, A)
        print(res)


if __name__ == "__main__":
    main()
