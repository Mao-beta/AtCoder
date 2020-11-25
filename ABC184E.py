import sys
import math
from collections import deque
from collections import defaultdict

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

    # ワープゾーンの位置を文字ごとに保存
    # start, goalの位置も取得
    warps = defaultdict(list)
    for h in range(H):
        for w in range(W):
            now = grid[h][w]
            if now == "S":
                start = (h, w)
            elif now == "G":
                goal = (h, w)
            elif now == "." or now == "#":
                continue
            else:
                warps[now].append((h, w))

    # BFS
    queue = deque()
    queue.append(start)
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    # 上下左右移動用
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # ワープ使用済みかどうか
    warp_used = defaultdict(int)

    while queue:
        now_h, now_w = queue.popleft()
        now_step = steps[now_h][now_w]
        now_grid = grid[now_h][now_w]

        # 普通の4方向
        for dh, dw in dirs:
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1
            # 範囲外なら無視
            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            # 今回の移動より早ければ無視
            # 既に来ていても効率悪いケースがあるためgoto_step以下であることが必要
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue
            # 壁なら無視
            if grid[goto_h][goto_w] == "#":
                continue

            queue.append((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step

        # a-zかつワープ未使用の時は追加処理
        if now_grid not in [".", "S", "G"] and warp_used[now_grid] == 0:
            for goto_h, goto_w in warps[now_grid]:
                goto_step = now_step + 1

                if now_h == goto_h and now_w == goto_w:
                    continue
                if 0 <= steps[goto_h][goto_w] <= goto_step:
                    continue

                queue.append((goto_h, goto_w))
                steps[goto_h][goto_w] = goto_step
            # その文字のワープは以降使用禁止
            warp_used[now_grid] = 1

    print(steps[goal[0]][goal[1]])


if __name__ == "__main__":
    main()
