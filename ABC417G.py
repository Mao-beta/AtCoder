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
    Q = NI()
    LRX = EI(Q)
    B = 62
    # idx_l, idx_r, sz_l, sz_r, sz_all, right_heavy(0/1)
    nodes = [[0, 0, 0, 0, 1, 0] for _ in range(Q+2)]
    nodes[1] = [1, 1, 0, 0, 1, 0]
    # node i から2^j回下ったときのnodeと、左で何文字消費したか
    doubling = [[[-1, 0] for _ in range(B)] for _ in range(Q+2)]

    is_heavy = [0] * (Q+2)

    for i, (l, r, x) in enumerate(LRX, start=2):
        x -= 1
        nl, nr = nodes[l], nodes[r]
        sz_l, sz_r = nl[4], nr[4]
        right_heavy = int(sz_l < sz_r)

        # compose
        nodes[i] = [l, r, sz_l, sz_r, sz_l + sz_r, right_heavy]
        doubling[i][0] = [r, sz_l] if right_heavy else [l, 0]
        for j in range(1, B):
            nx, sz = doubling[i][j-1]
            doubling[i][j][0] = doubling[nx][j-1][0]
            doubling[i][j][1] = sz + doubling[nx][j-1][1]

        print(i, l, r, x, doubling[i])
        # search
        now = i
        while now > 1:
            print(now, x, doubling[now][:4])
            print("nodes:", nodes)
            # heavyを潜る
            for j in range(B-1, -1, -1):
                if doubling[now][j][1] > x:
                    continue
                x -= doubling[now][j][1]
                now = doubling[now][j][0]
                break
            print(now, x)
            if now <= 1:
                break

            nx = nodes[now][0] if nodes[now][5] else nodes[now][1]
            x -= 0 if nodes[now][5] else nodes[now][2]
            now = nx
            print(now, x)

        if now == 0:
            print(0)
        else:
            print(1)


if __name__ == "__main__":
    main()
