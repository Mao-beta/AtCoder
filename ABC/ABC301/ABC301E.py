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


def main():
    H, W, T = NMI()
    A = [SI() for _ in range(H)]

    start = [0, 0]
    goal = [0, 0]
    sweets = []
    sweets_rev = defaultdict(int)
    
    for h in range(H):
        for w in range(W):
            a = A[h][w]
            if a == "S":
                start = [h, w]
            elif a == "G":
                goal = [h, w]
            elif a == "o":
                sweets_rev[(h, w)] = len(sweets)
                sweets.append([h, w])
    
    SN = len(sweets)
    INF = 10**15
    D = [[INF]*SN for _ in range(SN)]

    def bfs(start, sw_idx):
        queue = deque()
        queue.append(start)
        steps = [[INF] * W for _ in range(H)]
        steps[start[0]][start[1]] = 0
    
        DH = [0, 0, 1, -1]
        DW = [1, -1, 0, 0]
    
        while queue:
            now_h, now_w = queue.popleft()
            now_step = steps[now_h][now_w]
            
            if sw_idx >= 0 and A[now_h][now_w] == "o":
                sw_idx_now = sweets_rev[(now_h, now_w)]
                D[sw_idx][sw_idx_now] = now_step
                D[sw_idx_now][sw_idx] = now_step
    
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

        return steps

    for i, sweet in enumerate(sweets):
        bfs(sweet, i)

    S_steps = bfs(start, -1)
    G_steps = bfs(goal, -1)

    if S_steps[goal[0]][goal[1]] > T:
        print(-1)
        return

    def TSP(D):
        """
        巡回セールスマン問題 O(N^2*2^N)
        :param D: NxNの距離行列
        :return: 最短距離
        """
        N = len(D)
        dp = [[INF] * (1<<N) for _ in range(N)]
        for i in range(N):
            h, w = sweets[i]
            dp[i][1<<i] = S_steps[h][w]

        for case in range(1<<N):
            for u in range(N):
                if dp[u][case] >= INF:
                    continue
                for v in range(N):
                    if (case >> v) & 1:
                        continue
                    dp[v][case|(1<<v)] = min(dp[v][case|(1<<v)], dp[u][case] + D[u][v])

        return dp

    dp = TSP(D)
    ans = 0
    for v in range(SN):
        h, w = sweets[v]
        for case in range(1<<SN):
            step = dp[v][case]
            to_goal = G_steps[h][w]
            if step + to_goal <= T:
                k = str(bin(case)).count("1")
                ans = max(ans, k)

    print(ans)


if __name__ == "__main__":
    main()
