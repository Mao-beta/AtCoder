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


def is_simple_graph(N, edges, directed=False, origin=1) -> bool:
    """
    :param N: 頂点数
    :param edges: [[u, v], ...]
    :param directed: 有向ならTrue(default: False)
    :param origin: 1-indexか0-indexか(default: 1)
    :return: 単純グラフとしてvalidか
    """
    E = set()
    for u, v in edges:
        # 無向なら順序を揃える
        if not directed and u > v:
            u, v = v, u
        # 頂点の範囲に無い数字ならダメ
        if not (origin <= u < origin+N and origin <= v < origin+N):
            return False
        # 自己ループか二重辺があればダメ
        if u == v or (u, v) in E:
            return False
        E.add((u, v))
    
    return True
    

def main():
    N, M = NMI()
    UV = EI(M)
    if is_simple_graph(N, M, UV):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
