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


def main():
    H, W = NMI()
    S = [SI() for _ in range(H)]
    T = [0, 0]
    for h in range(H):
        for w in range(W):
            if S[h][w] == "T":
                T = [h, w]

    OK = defaultdict(int)
    for u in range(H+1):
        for d in range(H+1):
            for l in range(W+1):
                for r in range(W+1):
                    if u >= d or l >= r:
                        OK[(u, d, l, r)] = 1
                    else:
                        ok = True
                        for h in range(u, d):
                            for w in range(l, r):
                                if S[h][w] == "#":
                                    ok = False
                        OK[(u, d, l, r)] = int(ok)



    INF = 10*10
    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    # dp[h, w, u, d, l, r]
    # いまTが(h, w)で、処理境界が[u, d]x[l, r]のときの回数
    # 0 <= u <= d <= H, 0 <= l <= r <= W
    dp = defaultdict(lambda: INF)
    dp[(T[0],T[1],0,H,0,W)] = 0

    que = deque()
    que.append((T[0],T[1],0,H,0,W))
    while que:
        X = que.popleft()
        h, w, u, d, l, r = X
        step = dp[X]

        if OK[(u, d, l, r)]:
            print(step)
            return

        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw
            nu = max(u, nh - T[0])
            nd = min(d, nh + (H - T[0]))
            nl = max(l, nw - T[1])
            nr = min(r, nw + (W - T[1]))
            nstep = step + 1
            nX = (nh, nw, nu, nd, nl, nr)
            if dp[nX] <= nstep:
                continue

            if 0 <= nh < H and 0 <= nw < W and S[nh][nw] == "#" and u <= nh < d and l <= nw < r:
                continue
            dp[nX] = nstep
            que.append(nX)

    print(-1)


if __name__ == "__main__":
    main()
