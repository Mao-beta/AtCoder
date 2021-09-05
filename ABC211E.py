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


class GridBit:
    """
    gridの状態をHW桁のbitで持つ 最低Ｏ(HW)はかかる
    bitが同じものは同一objectと判定される（setやdictに入れてよい）
    copyが出来ないので、bitの数値から復元するにはload_bitを使う
    1個ずつ操作するならset_one, set_zeroを使う
    """
    def __init__(self, H, W):
        self.bit = 0
        self.H = H
        self.W = W
        self.ones = set()

    def load_bit(self, bit):
        for i in range(self.H * self.W):
            if (bit>>i) & 1:
                h, w = self.i2hw(i)
                self.set_one(h, w)

    def one_num(self):
        return len(self.ones)

    def hw2i(self, h, w):
        return h * self.W + w

    def i2hw(self, i):
        return i//self.W, i%self.W

    def set_one(self, h, w):
        i = self.hw2i(h, w)
        self.bit |= 1<<i
        self.ones.add(i)

    def set_zero(self, h, w):
        i = self.hw2i(h, w)
        self.bit &= ~(1<<i)
        self.ones.discard(i)

    def is_one(self, h, w):
        i = self.hw2i(h, w)
        return (self.bit >> i) & 1

    def dir4(self, h, w):
        kouho = [[h-1, w], [h+1, w], [h, w-1], [h, w+1]]
        res = set()
        for nh, nw in kouho:
            if 0 <= nh < self.H and 0 <= nw < self.W:
                res.add(self.hw2i(nh, nw))
        return res


    def get_asides(self):
        """
        いま1のマスに隣接する0のマスの(h, w)を列挙する
        """
        res = set()
        for one in self.ones:
            oh, ow = self.i2hw(one)
            res |= self.dir4(oh, ow)
        res -= self.ones
        res = set([self.i2hw(x) for x in res])
        return res

    def __eq__(self, other):
        return self.bit == other.bit

    def __hash__(self):
        return hash(self.bit)

    def __repr__(self):
        str_b = bin(self.bit)[2:].zfill(self.H*self.W)[::-1]
        res = []
        for i in range(0, self.H*self.W, self.W):
            res.append(str_b[i: i+self.W])
        return "\n".join(res)


def main():
    N = NI()
    K = NI()
    G = [SI() for _ in range(N)]
    grid = GridBit(N, N)
    for h in range(N):
        for w in range(N):
            if G[h][w] == ".":
                grid.set_one(h, w)

    seen = set()
    que = deque()

    for h in range(N):
        for w in range(N):
            if G[h][w] == "#":
                continue
            g = GridBit(N, N)
            g.set_one(h, w)
            que.append(g)
            seen.add(g)

    final = set()
    while que:
        now = que.popleft()
        if now.one_num() == K:
            final.add(now)
            continue

        for h, w in now.get_asides():
            if G[h][w] == "#":
                continue

            g = GridBit(N, N)
            g.load_bit(now.bit)
            g.set_one(h, w)

            if g in seen:
                continue

            que.append(g)
            seen.add(g)

    print(len(final))


if __name__ == "__main__":
    main()
