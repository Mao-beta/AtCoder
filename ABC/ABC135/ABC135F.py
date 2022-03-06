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


# KMP法
# 1対1の検索アルゴリズム。Tが固定のときTableを使いまわせる？
# 前計算O(|T|), 検索O(|S|)
# 事前にTから「j文字目で照合失敗したら次は何文字ずらすか」テーブルを作っておき、
# マッチ位置を試す位置を少なくする。
def make_kmp_table(t):
    i = 2
    j = 0
    m = len(t)
    tbl = [0] * (m + 1)
    tbl[0] = -1
    while i <= m:
        if t[i - 1] == t[j]:
            tbl[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = tbl[j]
        else:
            tbl[i] = 0
            i += 1
    return tbl


def kmp(s, t):
    matched_indices = []
    tbl = make_kmp_table(t)
    i = 0
    j = 0
    n = len(s)
    m = len(t)
    while i + j < n:
        if t[j] == s[i + j]:
            j += 1
            if j == m:
                matched_indices.append(i)
                i += j - tbl[j]
                j = tbl[j]
        else:
            i += j - tbl[j]
            if j > 0:
                j = tbl[j]
    return matched_indices


def topological_sort(graph):
    """
    BFSによるトポロジカルソート O(V+E)
    :param graph: 隣接リスト
    :return: 長さnならトポソ可能、そうでなければサイクルあり
    """
    n = len(graph)
    dims = [0] * n
    for i, adj in enumerate(graph):
        for goto in adj:
            dims[goto] += 1

    que = deque()
    for i, d in enumerate(dims):
        if d == 0:
            que.append(i)

    res = []
    while que:
        now = que.popleft()
        res.append(now)

        for goto in graph[now]:
            dims[goto] -= 1
            if dims[goto] == 0:
                que.append(goto)

    return res


def main():
    S = SI()
    T = SI()

    ls = len(S)
    lt = len(T)
    if ls < lt:
        k = lt // ls + 1
        S = S * k
        assert ls * k > lt
        ls *= k

    L = kmp(S*2, T)
    L = [l % ls for l in L]
    L = set(L)

    graph = [[] for _ in range(ls)]
    for x in L:
        graph[x].append((x+lt)%ls)
    # print(graph)

    topo = topological_sort(graph)
    # print(topo)

    if len(topo) != ls:
        print(-1)
        exit()

    dp = [0] * ls
    for v in topo:
        d = dp[v]
        for goto in graph[v]:
            dp[goto] = d + 1

    print(max(dp))


if __name__ == "__main__":
    main()
