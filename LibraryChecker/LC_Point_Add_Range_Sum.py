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


# SegTreeの関数
def segfunc(x, y):
    return x + y


# 単位元
# min->inf, max->-inf, add->0, mul->1
ide_ele = 0


# セグメント木
class SegTree:
    """
    init(init_val, segfunc, ide_ele): 配列init_valで初期化、構築
    get(k): k番目の値を取得
    update(k, x): k番目の値をxに更新
    query(l, r): 区間[l, r)をsegfuncしたものを返す
    """

    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセットする
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def get(self, k):
        """
        k番目の値を取得
        :param k:
        :return:
        """
        return self.tree[self.num + k]

    def update(self, k, x):
        """
        k番目の値をxに更新
        :param k: index(0-index)
        :param x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            l, r = min(k, k^1), max(k, k^1)
            self.tree[k >> 1] = self.segfunc(self.tree[l], self.tree[r])
            k >>= 1

    def add(self, k, x):
        """
        k番目の値にxを足す
        """
        self.update(k, self.get(k) + x)

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        :param l: 0-index
        :param r: 0-index
        :return:
        """
        res_L = self.ide_ele
        res_R = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res_L = self.segfunc(res_L, self.tree[l])
                l += 1
            if r & 1:
                res_R = self.segfunc(self.tree[r - 1], res_R)
            l >>= 1
            r >>= 1
        return self.segfunc(res_L, res_R)


def main():
    N, Q = NMI()
    A = NLI()
    S = SegTree(A, segfunc, ide_ele)
    for _ in range(Q):
        query = NLI()
        if query[0] == 0:
            S.add(query[1], query[2])
        else:
            print(S.query(query[1], query[2]))


if __name__ == "__main__":
    main()
