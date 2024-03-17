import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N = NI()
    S = ["#"*(N+2)] + ["#"+SI()+"#" for _ in range(N)] + ["#"*(N+2)]
    INF = 10**10
    steps = [[INF]*(N+2)**2 for _ in range((N+2)**2)]

    def f(h, w):
        return h*(N+2) + w

    def g(idx):
        return divmod(idx, N+2)

    Ps = []
    for h in range(N+2):
        for w in range(N+2):
            if S[h][w] == "P":
                Ps.append(f(h, w))

    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    steps[Ps[0]][Ps[1]] = 0
    que = deque()
    que.append(Ps)
    while que:
        p1, p2 = que.popleft()
        h1, w1 = g(p1)
        h2, w2 = g(p2)
        if h1 == h2 and w1 == w2:
            print(steps[p1][p2])
            return
        for dh, dw in zip(DH, DW):
            nh1, nw1 = h1+dh, w1+dw
            nh2, nw2 = h2+dh, w2+dw
            if S[nh1][nw1] == "#":
                nh1, nw1 = h1, w1
            if S[nh2][nw2] == "#":
                nh2, nw2 = h2, w2
            np1, np2 = f(nh1, nw1), f(nh2, nw2)
            if steps[np1][np2] > steps[p1][p2] + 1:
                steps[np1][np2] = steps[p1][p2] + 1
                que.append([np1, np2])

    print(-1)


if __name__ == "__main__":
    main()
