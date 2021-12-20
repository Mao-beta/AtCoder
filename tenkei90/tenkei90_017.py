import sys
import math
from collections import defaultdict

sys.setrecursionlimit(100000)
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

    def add(self, k, x):
        val = self.tree[self.num+k]
        self.update(k, val+x)

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
        return str(self.tree[self.num:])


def solve(N, M, LR):
    LR = [[l-1, r-1] for l, r in LR]
    events = defaultdict(list)
    for i, (l, r) in enumerate(LR):
        events[l].append([i, l, r])
        events[r].append([i+M, l, r])

    ans = 0

    tree = SegTree([0]*N, segfunc=segfunc, ide_ele=ide_ele)
    for i in range(N):
        querys = events[i]
        querys.sort(key=lambda x: -x[0])
        for idx, l, r in querys:
            if idx >= M:
                tree.add(l, -1)
            else:
                tree.add(l, 1)
        for idx, l, r in querys:
            if idx >= M:
                ans += tree.query(l+1, r)

    print(ans)


def main():
    N, M = NMI()
    LR = [NLI() for _ in range(M)]
    solve(N, M, LR)


if __name__ == "__main__":
    main()
