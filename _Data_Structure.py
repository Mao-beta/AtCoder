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


class UnionFind:
    def __init__(self, n):
        #親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n

    def find(self, x):
        #根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            #親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        #根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        #木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


class WeightedUnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        # 根からノードへの重みを管理
        self.weight = [0] * n

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 再帰的に累積和を取る
            r = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = r
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def get_weight(self, x):
        self.find(x)
        return self.weight[x]

    def diff(self, x, y):
        # xからyへの重み
        return self.get_weight(y) - self.get_weight(x)

    # xからyへの重みはw
    def unite(self, x, y, w=0):
        w = w + self.get_weight(x) - self.get_weight(y)
        x = self.find(x)
        y = self.find(y)

        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if -self.par[x] < -self.par[y]:
            x, y = y, x
            w = -w

        self.par[x] += self.par[y]
        self.par[y] = x
        self.weight[y] = w

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def weights(self):
        return self.weight

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


# SegTreeの関数
def segfunc(x, y):
    return min(x, y)


# 単位元
# min->inf, max->-inf, add->0, mul->1
ide_ele = float("inf")


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


class BIT():
    def __init__(self, n):
        """
        0-index
        sum -> i番目までの和
        add -> i番目にxを足す
        :param n:
        """
        self.n = n
        self.data = [0] * (n + 1)
        self.each = [0] * (n + 1)

    def sum(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        self.each[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def __repr__(self):
        return str(self.each)


class LCATree:
    def __init__(self, n, edges, root):
        """
        最小共通祖先(LCA)を求める木　要deque
        :param n: nodeの数(1からn)
        :param edges: 辺の情報(1からn-1)
        :param root: 根
        """
        self.n = n
        self.max_double = len(bin(self.n))  # 最大何回ダブリングで遡るか およそlog2(n)
        self.adj = self.make_adjlist_nond(self.n, edges)  # 隣接リスト
        self.root = root
        # parent[i][x]はxから2^i回根の方向に上った点 -1ならその親が存在しない
        self.parent = [[-1] * (self.n + 1) for _ in range(self.max_double)]
        self.depth = [-1] * (self.n + 1)

        # dfsで各ノードの親と深さを記録
        stack = deque()
        stack.append(self.root)
        self.depth[self.root] = 0
        while stack:
            now = stack.pop()
            par = self.parent[0][now]

            for goto in self.adj[now]:
                if goto == par:
                    continue
                stack.append(goto)
                self.parent[0][goto] = now
                self.depth[goto] = self.depth[now] + 1

        for d in range(self.max_double):
            if d == 0: continue
            pre_par = self.parent[d - 1]
            for i in range(self.n + 1):
                if pre_par[i] < 0:
                    self.parent[d][i] = -1
                    continue
                self.parent[d][i] = pre_par[pre_par[i]]

    def get_LCA(self, x, y):
        """
        ノードxとノードyのLCA(最小共通祖先)を返す
        :param x:
        :param y:
        :return: res
        """
        dx, dy = self.depth[x], self.depth[y]
        # 深いほうをxとする
        if dx < dy:
            x, y = y, x
            dx, dy = dy, dx
        gap_d = dx - dy
        # 同じ高さまで引き上げる
        for i in range(self.max_double + 1):
            if (gap_d >> i) & 1:
                x = self.parent[i][x]
        # 引き上げた結果同じ所ならそこがLCA
        if x == y:
            return x

        # xとyを同時にダブリングで引き上げる
        # ジャンプ先の地点が異なるならOK、同じならジャンプ幅を半分にする
        for i in range(self.max_double - 1, -1, -1):
            if self.parent[i][x] != self.parent[i][y]:
                x = self.parent[i][x]
                y = self.parent[i][y]
        # ギリギリ同じにならない地点の親がLCA
        return self.parent[0][x]

    @staticmethod
    def make_adjlist_nond(n, edges):
        res = [[] for _ in range(n + 1)]
        for edge in edges:
            res[edge[0]].append(edge[1])
            res[edge[1]].append(edge[0])
        return res


class Deque:
    """
    ランダムアクセスをO(1)でできるDeque
    """
    def __init__(self, src_arr=[], max_size=300000):
        self.N = max(max_size, len(src_arr)) + 1
        self.buf = list(src_arr) + [None] * (self.N - len(src_arr))
        self.head = 0
        self.tail = len(src_arr)
    def __index(self, i):
        l = len(self)
        if not -l <= i < l: raise IndexError('index out of range: ' + str(i))
        if i < 0:
            i += l
        return (self.head + i) % self.N
    def __extend(self):
        ex = self.N - 1
        self.buf[self.tail+1 : self.tail+1] = [None] * ex
        self.N = len(self.buf)
        if self.head > 0:
            self.head += ex
    def is_full(self):
        return len(self) >= self.N - 1
    def is_empty(self):
        return len(self) == 0
    def append(self, x):
        if self.is_full(): self.__extend()
        self.buf[self.tail] = x
        self.tail += 1
        self.tail %= self.N
    def appendleft(self, x):
        if self.is_full(): self.__extend()
        self.buf[(self.head - 1) % self.N] = x
        self.head -= 1
        self.head %= self.N
    def pop(self):
        if self.is_empty(): raise IndexError('pop() when buffer is empty')
        ret = self.buf[(self.tail - 1) % self.N]
        self.tail -= 1
        self.tail %= self.N
        return ret
    def popleft(self):
        if self.is_empty(): raise IndexError('popleft() when buffer is empty')
        ret = self.buf[self.head]
        self.head += 1
        self.head %= self.N
        return ret
    def __len__(self):
        return (self.tail - self.head) % self.N
    def __getitem__(self, key):
        return self.buf[self.__index(key)]
    def __setitem__(self, key, value):
        self.buf[self.__index(key)] = value
    def __str__(self):
        return 'Deque({0})'.format(str(list(self)))



def main():
    a = [14, 5, 9, 13, 7, 12, 11, 1, 7, 8]

    seg = SegTree(a, segfunc, ide_ele)

    print(seg.query(0, 8))
    seg.update(5, 0)
    print(seg.query(0, 8))


if __name__ == "__main__":
    main()