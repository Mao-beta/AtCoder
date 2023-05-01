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


def print_err(*args):
    print(*args, file=sys.stderr)


from collections import deque
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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N = NI()
    ST = [SLI() for _ in range(N)]
    SS = []
    for s, t in ST:
        SS.append(s)
        SS.append(t)
    Z, UZ = compress(SS)

    G = [[] for _ in range(len(Z))]
    for s, t in ST:
        G[Z[t]].append(Z[s])

    res = topological_sort(G)
    if len(res) == len(Z):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
