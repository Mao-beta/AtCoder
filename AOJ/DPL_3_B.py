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


def largest_rectangle_in_histogram(_H: list) -> int:
    """
    ヒストグラム内の最大長方形の面積 stack使用でO(N)
    """
    from collections import deque
    H = _H.copy()
    H.append(0)
    res = 0
    D = deque()
    # i, h
    D.append([0, 0])
    for i, h in enumerate(H):
        li = i
        while D[-1][1] > h:
            li, lh = D.pop()
            res = max(res, (i-li)*lh)
        D.append([li, h])

    return res


def largest_rectangle_in_grid(_G: list) -> int:
    """
    Gridは[壁：0, 空：1]
    Grid内の[1のマス]のみ使った最大長方形の面積 O(HW)
    各行ごとにヒストグラムと見てそれらの最大長方形を計算
    """
    G = [row[:] for row in _G]
    H = len(G)
    W = len(G[0])
    
    # 注目しているマスから見て上に積みあがっている1のマスの個数を調べる
    for h in range(H-1):
        for w in range(W):
            if G[h+1][w] != 0:
                G[h+1][w] = G[h][w] + 1

    res = 0
    for row in G:
        res = max(res, largest_rectangle_in_histogram(row))
    return res
    

def main():
    H, W = NMI()
    C = []
    for _ in range(H):
        row = NLI()
        row = [1-x for x in row] # 1のマスのみ使うことにする
        C.append(row)
    ans = largest_rectangle_in_grid(C)
    print(ans)


if __name__ == "__main__":
    main()
