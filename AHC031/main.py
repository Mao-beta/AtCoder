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


def _allocate_rectangle(free_spaces, area):
    """
    単一の予約に対して、空き領域から最適な長方形を割り当てる。
    :param free_spaces: 空き領域のリスト（半開区間）
    :param area: 割り当てる面積
    :return: 割り当てた長方形の座標と、割り当て前の空き領域の座標
    """
    best_space = None
    for space in free_spaces:
        space_area = (space[2] - space[0]) * (space[3] - space[1])
        if space_area >= area:
            if best_space is None or space_area < best_space[4]:
                best_space = space + (space_area,)

    if best_space is None:
        return None, None

    x1, y1, x2, y2, _ = best_space
    w = x2 - x1
    h = y2 - y1

    def find_edge_length(length, area):
        left, right = 1, length
        while left < right:
            mid = (left + right) // 2
            if mid * length >= area:
                right = mid
            else:
                left = mid + 1
        return left

    new_w = find_edge_length(w, area)
    new_h = (area + new_w - 1) // new_w

    if new_h > h:
        new_h = find_edge_length(h, area)
        new_w = (area + new_h - 1) // new_h

    return (x1, y1, x1 + new_w, y1 + new_h), best_space[:4]


def allocate_rectangle(free_spaces, area, W):
    """
    単一の予約に対して、空き領域から最適な長方形を割り当てる。
    :param free_spaces: 空き領域のリスト（半開区間）
    :param area: 割り当てる面積
    :param W: グリッドの幅
    :return: 割り当てた長方形の座標と、割り当て前の空き領域の座標
    """
    best_space = None
    best_score = 0  # 最良のスコアを管理する変数

    for space in free_spaces:
        space_area = (space[2] - space[0]) * (space[3] - space[1])
        if space_area >= area:
            w = space[2] - space[0]
            h = space[3] - space[1]
            ratio = max(w, h) / min(w, h)  # 縦横比を計算
            score = space_area / (ratio ** 2)  # 面積と縦横比のバランスを考慮したスコアを計算
            if score > best_score:
                best_space = space
                best_score = score

    if best_space is None:
        return None, None

    x1, y1, x2, y2 = best_space
    w = x2 - x1
    h = y2 - y1

    # 縦横比が1に近く、割り当て可能な範囲内の最大の長方形を割り当てる
    if w > h:
        new_w = min((int(math.sqrt(area * h / w)) + (1 if math.sqrt(area * h / w) > int(math.sqrt(area * h / w)) else 0)), w)
        new_h = min((area + new_w - 1) // new_w, h)
    else:
        new_h = min((int(math.sqrt(area * w / h)) + (1 if math.sqrt(area * w / h) > int(math.sqrt(area * w / h)) else 0)), h)
        new_w = min((area + new_h - 1) // new_h, w)

    return (x1, y1, min(x1 + new_w, W), min(y1 + new_h, W)), best_space

def split_free_space(free_spaces, allocation, old_space):
    """
    割り当てた長方形を除いた新しい空き領域を生成する。
    :param free_spaces: 空き領域のリスト（半開区間）
    :param allocation: 割り当てた長方形の座標
    :param old_space: 割り当て前の空き領域の座標
    """
    x1, y1, x2, y2 = allocation
    ox1, oy1, ox2, oy2 = old_space

    if x1 > ox1:
        free_spaces.append((ox1, oy1, x1, oy2))
    if x2 < ox2:
        free_spaces.append((x2, oy1, ox2, oy2))
    if y1 > oy1:
        free_spaces.append((x1, oy1, x2, y1))
    if y2 < oy2:
        free_spaces.append((x1, y2, x2, oy2))

    if old_space in free_spaces:
        free_spaces.remove(old_space)


def allocate_rectangles(W, reservations, grid):
    """
    全ての予約に対して、空き領域から最適な長方形を割り当てる。
    :param W: グリッドの幅
    :param reservations: 予約のリスト（面積とIDのタプル）
    :param grid: 割り当て状況を管理するグリッド
    :return: 割り当てた長方形の座標のリストと、割り当てられなかった予約IDのリスト
    """
    free_spaces = [(0, 0, W, W)]  # 半開区間で初期化
    reservations.sort(key=lambda x: x[0], reverse=True)

    allocations = []
    unallocated = []

    for reservation in reservations:
        area, id = reservation
        allocation, old_space = allocate_rectangle(free_spaces, area, W)

        if allocation is None:
            # 空き領域が見つからない場合は、割り当てられなかったリストに追加して次の予約に進む
            unallocated.append(id)
            continue

        split_free_space(free_spaces, allocation, old_space)

        allocations.append(allocation + (id,))

        # グリッドに割り当て状況を反映
        for i in range(allocation[0], allocation[2]):
            for j in range(allocation[1], allocation[3]):
                grid[i][j] = 1

    return allocations, unallocated


def reallocate_unallocated(W, unallocated, grid):
    """
    割り当てられなかった予約に対して再度割り当てを試みる。
    :param W: グリッドの幅
    :param unallocated: 割り当てられなかった予約IDのリスト
    :param grid: 割り当て状況を管理するグリッド
    :return: 再割り当てした長方形の座標のリスト
    """
    reallocations = []

    for id in unallocated:
        for i in range(W):
            for j in range(W):
                if grid[i][j] == 0:
                    # 割り当て済みでない座標を見つけたら、その座標を左上とする最大の長方形を割り当てる
                    x1, y1 = i, j
                    x2, y2 = i + 1, j + 1
                    while x2 < W and grid[x2][y1] == 0:
                        x2 += 1
                    while y2 < W and grid[x1][y2] == 0:
                        y2 += 1

                    # グリッドに割り当て状況を反映
                    for x in range(x1, x2):
                        for y in range(y1, y2):
                            grid[x][y] = 1

                    reallocations.append((x1, y1, x2, y2, id))
                    break
            else:
                continue
            break

    return reallocations


def main():
    W, D, N = NMI()
    A = EI(D)
    ans = []
    for d in range(D):
        reservations = [(area, i) for i, area in enumerate(A[d])]
        grid = [[0] * W for _ in range(W)]  # 割り当て状況を管理するグリッドを初期化
        alloc, unalloc = allocate_rectangles(W, reservations, grid)
        # print(len(alloc), len(unalloc))
        realloc = reallocate_unallocated(W, unalloc, grid)

        # 割り当てた長方形と再割り当てした長方形の座標をansに追加
        for x1, y1, x2, y2, id in sorted(alloc + realloc, key=lambda x: x[-1]):
            ans.append([y1, x1, y2, x2])

    # ansの内容を出力
    for row in ans:
        print(*row)



if __name__ == "__main__":
    main()