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
    A = [SI() for _ in range(H)]
    N = NI()
    RCE = EI(N)
    RCE = [[x-1, y-1, w] for x, y, w in RCE]

    S = [0, 0]
    T = [0, 0]
    for h in range(H):
        for w in range(W):
            if A[h][w] == "S":
                S = [h, w]
            elif A[h][w] == "T":
                T = [h, w]
    
    RCE.append([*S, 0])
    RCE.append([*T, 0])

    D = [[[10**10]*W for _ in range(H)] for _ in range(N+2)]
         
    for i in range(N+2):
        h, w, e = RCE[i]
        start = (h, w)
    
        queue = deque()
        queue.append(start)
        steps = D[i]
        steps[start[0]][start[1]] = 0
    
        DH = [0, 0, 1, -1]
        DW = [1, -1, 0, 0]
    
        while queue:
            now_h, now_w = queue.popleft()
            now_step = steps[now_h][now_w]
    
            for dh, dw in zip(DH, DW):
                goto_h = now_h + dh
                goto_w = now_w + dw
                goto_step = now_step + 1
    
                if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                    continue
                if A[goto_h][goto_w] == "#":
                    continue
                if 0 <= steps[goto_h][goto_w] <= goto_step:
                    continue
    
                queue.append((goto_h, goto_w))
                steps[goto_h][goto_w] = goto_step

        # print(*steps, sep="\n")
        # print()

    G = [[] for _ in range(N+2)]
    for i in range(N+2):
        for j in range(i+1, N+2):
            ri, ci, ei = RCE[i]
            rj, cj, ej = RCE[j]
            sij = D[i][rj][cj]
            sji = D[j][ri][ci]
            if sij <= ei:
                G[i].append(j)
            if sji <= ej:
                G[j].append(i)

    # print(G)

    que = deque()
    que.append(N)
    seen = [0] * (N+2)
    seen[N] = 1
    while que:
        now = que.popleft()
        for g in G[now]:
            if seen[g]:
                continue
            seen[g] = 1
            que.append(g)
            if g == N+1:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
