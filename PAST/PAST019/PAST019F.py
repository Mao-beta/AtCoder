import itertools
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


def compress(S):
    """ 座標圧縮 """
    S = set(S)
    zipped = {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
    return zipped


def main():
    N = NI()
    X, Y = SMI()
    ST = [SLI() for _ in range(N)]
    Z = compress(list(itertools.chain.from_iterable(ST)) + [X, Y])
    G = [[] for _ in range(len(Z))]
    for s, t in ST:
        s, t = Z[s], Z[t]
        G[s].append(t)
    X, Y = Z[X], Z[Y]

    steps = [-1] * len(Z)
    que = deque()
    que.append(X)
    steps[X] = 0
    while que:
        now = que.popleft()
        step = steps[now]
        for goto in G[now]:
            if steps[goto] != -1:
                continue
            que.append(goto)
            steps[goto] = step + 1
    if steps[Y] >= 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
