import random
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product, chain

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


IS_LOCAL = True
try:
    import matplotlib
except:
    IS_LOCAL = False


import random
def sample(k, v, eps, e):
    mu = (k - v) * eps + v * (1 - eps)
    var = k * eps * (1 - eps)
    return e * math.sqrt(var) + mu


def main():
    N, M, e = SMI()
    N = int(N)
    M = int(M)
    e = float(e)

    yudens = []
    yuden_size = []
    yuden_ds = []
    for _ in range(M):
        d, *XY = NMI()
        yuden_ds.append(d)
        yuden = set()
        szx, szy = 0, 0
        for i in range(0, d, 2):
            x, y = XY[2*i], XY[2*i+1]
            yuden.add((x, y))
            szx = max(szx, x)
            szy = max(szy, y)
        yudens.append(yuden)
        yuden_size.append((szx, szy))
    yuden_sum = sum(yuden_ds)

    if IS_LOCAL:
        DIJ = EI(M)
        V = EI(N)
        E = [float(SI()) for _ in range(2*N*N)]


    # 適当に1点とって当たればそこからDFS
    ans = []
    vsum = [0]
    query_cnt = [0]
    unseen = set((i//N, i%N) for i in range(N**2))

    DI = [0, 0, 1, -1]
    DJ = [1, -1, 0, 0]

    def query1(i, j):
        print(f"q 1 {i} {j}", flush=True)
        query_cnt[0] += 1
        if IS_LOCAL:
            return V[i][j]
        else:
            return NI()

    def query_ans(ans):
        d = len(ans)
        ans = chain.from_iterable(ans)
        print(f"a {d} {' '.join(map(str, ans))}", flush=True)
        query_cnt[0] += 1
        res = NI()
        assert res == 1

    def dfs(i, j):
        if vsum[0] >= yuden_sum:
            return

        v = query1(i, j)
        unseen.discard((i, j))
        vsum[0] += v
        if v > 0:
            ans.append((i, j))
        else:
            return

        for di, dj in zip(DI, DJ):
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and (ni, nj) in unseen:
                dfs(ni, nj)


    while vsum[0] < yuden_sum and unseen:
        si, sj = unseen.pop()
        dfs(si, sj)

    query_ans(ans)


if __name__ == "__main__":
    main()
