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


class Polyomino:
    def __init__(self, P: list[tuple[int, int]]):
        """
        ポリオミノのようなXY座標のリストを扱う
        :param P: XY座標タプルのリスト
        """
        self.P = P

    def __add__(self, other):
        # 座標を連結
        res = list(set(self.P + other.P))
        return Polyomino(res)

    def copy(self):
        return Polyomino(self.P[:])

    def normalize(self):
        # 左上隅に寄せる
        mh = 5
        mw = 5
        for h, w in self.P:
            mh = min(mh, h)
            mw = min(mw, w)
        self.P = [(h - mh, w - mw) for h, w in self.P]
        return self

    def rotate90(self):
        self.P = [(-w, h) for h, w in self.P]
        self.normalize()
        return self

    def is_valid(self, H, W):
        # [0, H), [0, W)に収まっているかを判定
        for h, w in self.P:
            if not (0 <= h < H and 0 <= w < W):
                return False
        return True

    def is_duplicated(self, other):
        # P同士で座標の重複があるか
        res = list(set(self.P + other.P))
        return len(res) < len(self.P) + len(other.P)

    def shift(self, dh, dw):
        self.P = [(h + dh, w + dw) for h, w in self.P]
        return self

    def digitize(self, H, W):
        # H*W bitの整数に変換
        res = 0
        for h, w in self.P:
            res |= 1 << (h * W + w)
        return res

    def __repr__(self):
        return f"Polyomino({self.P})"


def main():
    P = []
    for _ in range(3):
        tmp = []
        for h in range(4):
            s = SI()
            for w in range(4):
                if s[w] == "#":
                    tmp.append((h, w))
        P.append(Polyomino(tmp))

    Q = []
    for p in P:
        p.normalize()
        tmp = []
        for rot in range(4):
            for dh in range(4):
                for dw in range(4):
                    np = p.copy().shift(dh, dw)
                    if np.is_valid(4, 4):
                        tmp.append(np)
            p.rotate90()
        Q.append(tmp)

    M = 1 << 16
    M -= 1

    for X in product(*Q):
        ok = True
        p = Polyomino([])
        for x in X:
            if p.is_duplicated(x):
                ok = False
                break
            else:
                p += x

        if ok and p.digitize(4, 4) == M:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
