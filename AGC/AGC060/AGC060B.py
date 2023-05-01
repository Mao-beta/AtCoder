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


def main(N, M, K, S):
    G = [[-9]*M for _ in range(N)]
    now = [0, 0]
    for i, s in enumerate(S):
        G[now[0]][now[1]] = 0
        if i == 0:
            if s == "R":
                now[1] += 1
            else:
                now[0] += 1
            continue

        p = S[i-1]
        if s == "R":
            if p != s and now[0]-1 >= 0 and now[1]+1 <= M-1:
                G[now[0]-1][now[1]+1] = -1
            now[1] += 1
        else:
            if p != s and now[0]+1 <= N-1 and now[1]-1 >= 0:
                G[now[0]+1][now[1]-1] = -1
            now[0] += 1

    G[now[0]][now[1]] = 0

    d = 1
    h, w = now
    while h > 0 or w > 0:
        d = max(d, G[h][w])
        # print(h, w, d)
        if h >= 1 and G[h-1][w] == -1:
            G[h-1][w] = -d
            if w >= 1:
                G[h-1][w-1] = d+1
        if w >= 1 and G[h][w-1] == -1:
            G[h][w-1] = -d
            if h >= 1:
                G[h-1][w-1] = d+1

        if h >= 1 and G[h-1][w] >= 0:
            h -= 1
        elif w >= 1 and G[h][w-1] >= 0:
            w -= 1

    d = max(d, G[h][w])
    # print(*G, sep="\n")
    if d-1 <= K:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    T = NI()
    for _ in range(T):
        N, M, K = NMI()
        S = SI()
        main(N, M, K, S)
