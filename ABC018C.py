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


def main():
    H, W, K = NMI()
    S = [SI() for _ in range(H)]
    INF = 10000
    G = [[INF]*W for _ in range(H)]
    
    que = deque()
    for h in range(H):
        for w in range(W):
            if S[h][w] == "x":
                que.append([h, w, 0])
    
    DH = [-1, 1, 0, 0]
    DW = [0, 0, -1, 1]
    while que:
        h, w, now = que.popleft()
        if G[h][w] <= now: continue
        G[h][w] = now
        # print(h, w)
        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw
            if 0 <= nh < H and 0 <= nw < W:
                if G[nh][nw] <= now: continue
                que.append([nh, nw, now+1])

        # print(*G, sep="\n")

    # print(*G, sep="\n")
    ans = 0
    for h in range(K-1, H-K+1):
        for w in range(K-1, W-K+1):
            # print(h, w)
            if G[h][w] >= K:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
