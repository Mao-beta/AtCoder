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


# SegTreeの関数
def segfunc(X, Y):
    return [X[0]+Y[0], X[1] + Y[1]]
# 単位元
# min->inf, max->-inf, add->0, mul->1
ide_ele = [0, 0]

# セグメント木
class SegTree:
    """
    init(init_val, segfunc, ide_ele): 配列init_valで初期化、構築
    update(k, x): k番目の値をxに更新
    query(l, r): 区間[l, r)をsegfuncしたものを返す
    """
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセットする
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        :param k: index(0-index)
        :param x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k>>1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        :param l: 0-index
        :param r: 0-index
        :return:
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


def main():
    N, K = NMI()
    C = NLI()
    Q = NI()
    D = [NI() for _ in range(Q)]

    if N == 1:
        print(0)
        exit()

    C.sort()
    gaps = [C[i+1] - C[i] for i in range(N-1)]

    sum_gap = C[-1] - C[0]
    init_val = [[0, 0] for _ in range(sum_gap+1)]
    for gap in gaps:
        init_val[gap][0] += 1
        init_val[gap][1] += gap
    print(init_val)
    segtree = SegTree(init_val, segfunc, ide_ele)

    for d in D:
        node = segtree.query(d, d+1)
        segtree.update(d, [node[0]-1, node[1]-d])
        print(segtree.query(0, sum_gap+1))



if __name__ == "__main__":
    main()