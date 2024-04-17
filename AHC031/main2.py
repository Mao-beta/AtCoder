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


def allocate_rectangles(A_d, left_width, W):
    allocations = [None] * len(A_d)
    left_height = 0
    right_height = 0

    # 予約を面積とインデックスのタプルのリストに変換する
    reservations = [(area, i) for i, area in enumerate(A_d)]

    # 最大の予約を左側の上側から割り当てる
    max_reservation = max(reservations)
    max_area, max_index = max_reservation
    allocations[max_index] = (0, left_height, left_width, left_height + (max_area + left_width - 1) // left_width)
    left_height += (max_area + left_width - 1) // left_width
    reservations.remove(max_reservation)

    # 残りの予約を面積の小さい順にソートする
    reservations.sort()

    # 左側の領域に割り当てる
    for area, index in reservations:
        if left_height + (area + left_width - 1) // left_width <= W:
            allocations[index] = (0, left_height, left_width, left_height + (area + left_width - 1) // left_width)
            left_height += (area + left_width - 1) // left_width
        else:
            # 右側の領域に割り当てる
            allocations[index] = (
            left_width, right_height, W, right_height + (area + W - left_width - 1) // (W - left_width))
            right_height += (area + W - left_width - 1) // (W - left_width)

    return allocations


def main():
    W, D, N = NMI()
    A = EI(D)
    MaxA = max(max(a) for a in A)
    left_width = (MaxA + W - 1) // W
    ans = []

    for d in range(D):
        allocations = allocate_rectangles(A[d], left_width, W)
        for x1, y1, x2, y2 in allocations:
            x1 = min(x1, W)
            x2 = min(x2, W)
            y1 = min(y1, W)
            y2 = min(y2, W)
            ans.append([y1, x1, y2, x2])
        # print(len(allocations))

    # print(len(ans))
    # ansの内容を出力
    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()