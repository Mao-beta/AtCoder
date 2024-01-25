import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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

from collections import defaultdict


class UnionFind:
    def __init__(self):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = defaultdict(lambda: -1)

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]


# Nの素因数分解を辞書で返す(単体)
def prime_fact(n):
    root = int(n**0.5) + 1
    prime_dict = {}
    for i in range(2, root):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def main():
    H, W = NMI()
    C = [SI() for _ in range(H)]

    DH = [0, 0, 1, -1, 1, 1, -1, -1]
    DW = [1, -1, 0, 0, 1, -1, 1, -1]

    uf = UnionFind()
    for idx in range(H*W):
        h, w = divmod(idx, W)
        if C[h][w] == ".":
            continue
        for dh, dw in zip(DH, DW):
            nh, nw = h+dh, w+dw
            if 0 < nh < H and 0 <= nw < W:
                nidx = nh*W + nw
                if C[nh][nw] == ".":
                    continue
                uf.unite(idx, nidx)

    a, b, c = 0, 0, 0
    # a: 12, b: 16, c: 11
    for s in uf.par.values():
        if s >= 0:
            continue
        s *= -1
        if s <= 1:
            continue
        D = prime_fact(s)
        if 11 in D and D[11] % 2:
            c += 1
        elif 3 in D and D[3] % 2:
            a += 1
        else:
            b += 1

    print(a, b, c)


if __name__ == "__main__":
    main()
