import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    H, W = NMI()
    grid = [SI() for _ in range(H)]
    DH = [-1, 1, 0, 0]
    DW = [0, 0, -1, 1]

    def bfs(sh, sw):
        queue = deque()
        seen = make_grid(H, W, -1)
        queue.append([sh, sw])
        seen[sh][sw] = 0
        while queue:
            now_h, now_w = queue.popleft()
            for dh, dw in zip(DH, DW):
                next_h = now_h + dh
                next_w = now_w + dw
                if not(0 <= next_h < H and 0 <= next_w < W):
                    continue
                if seen[next_h][next_w] != -1 or grid[next_h][next_w] == "#":
                    continue
                queue.append([next_h, next_w])
                seen[next_h][next_w] = seen[now_h][now_w] + 1

        return max([max(l) for l in seen])

    ans = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == ".":
                ans = max(ans, bfs(h, w))
    print(ans)




if __name__ == "__main__":
    main()