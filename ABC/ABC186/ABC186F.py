import sys
import math
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


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

    def __repr__(self):
        return " ".join(map(str, self.tree[self.num:]))


def main():
    H, W, M = NMI()
    blocks = [NLI() for _ in range(M)]
    tree = SegTree([0]*W, segfunc, ide_ele)

    blocks.sort()

    y_set = set()
    block_dict = defaultdict(bool)
    invalid_minx = 10**6
    for x, y in blocks:
        x, y = x-1, y-1
        if y in y_set:
            block_dict[(x, y)] = True
        else:
            y_set.add(y)

        if y == 0 and invalid_minx == 10**6:
            invalid_minx = x


    prev_x = -1
    ans = H*W
    for x, y in blocks:
        x, y = x-1, y-1
        #print(x, y)
        if x <= invalid_minx:

            if x == prev_x:
                if block_dict[(x, y)] == False:
                    ans -= 1
                tree.update(y, 1)
            else:
                tree.update(y, 1)
                ans -= tree.query(y, W)

        else:
            if x == prev_x:
                if block_dict[(x, y)] == False:
                    ans -= 1
                tree.update(y, 1)
            else:
                tree.update(y, 1)
                ans -= tree.query(0, W) * (x - prev_x)

        print(tree)
        prev_x = x
    if prev_x != H-1 and invalid_minx != 10**6:
        ans -= tree.query(0, W) * (H-1 - prev_x)

    print(ans)



if __name__ == "__main__":
    main()
