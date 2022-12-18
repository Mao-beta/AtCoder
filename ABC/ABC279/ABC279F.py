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
    N, Q = NMI()
    Box = [{i} for i in range(N+1)]
    total = N

    # 箱Xを管理しているBoxのindexと、その逆
    labels = list(range(N+1))
    inv_label = list(range(N+1))

    # ボールXの入っている箱のlabel
    balls = list(range(N+1)) + [0] * Q

    # マージテクをつかう
    # 大きいほうに小さいほうをつけることで、
    # 1のクエリが計算量ならしO(logN)くらいになるので間に合う
    for qi in range(Q):
        q, *X = NMI()
        if q == 1:
            x, y = X
            lx, ly = labels[x], labels[y]

            if len(Box[lx]) >= len(Box[ly]):
                # ボールが入っている箱のlabelを書き換え
                for b in Box[ly]:
                    balls[b] = lx
                # マージ
                Box[lx] |= Box[ly]
                Box[ly] = set()

            else:
                # ボールが入っている箱のlabelを書き換え
                for b in Box[lx]:
                    balls[b] = ly
                # マージ
                Box[ly] |= Box[lx]
                Box[lx] = set()
                # xとyのlabelの辻褄をあわせる(本来とは逆なので)
                labels[x], labels[y] = ly, lx
                inv_label[lx], inv_label[ly] = y, x

        elif q == 2:
            x = X[0]
            lx = labels[x]
            Box[lx].add(total+1)
            balls[total+1] = lx
            total += 1

        else:
            x = X[0]
            print(inv_label[balls[x]])


if __name__ == "__main__":
    main()
