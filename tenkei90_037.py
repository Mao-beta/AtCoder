import sys
import math
from collections import defaultdict
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
    return max(x, y)


# 単位元
# min->inf, max->-inf, add->0, mul->1
INF = 10**15
ide_ele = -INF


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
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセットする
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        :param k: index(0-index)
        :param x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
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
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


def main():
    W, N = NMI()
    S = [NLI() for _ in range(N)]

    dp = [-1]*(W+5)
    dp[0] = 0
    for l, r, v in S:
        seg = SegTree(dp, segfunc, ide_ele)
        for w in range(1, W+1):
            wmin = max(w - r, 0)
            wmax = min(w - l, W)
            if wmin > wmax:
                continue
            best = seg.query(wmin, wmax+1)
            if best == -1:
                continue
            dp[w] = max(best + v, dp[w])

    print(dp[W] if dp[W] != 0 else -1)


if __name__ == "__main__":
    main()