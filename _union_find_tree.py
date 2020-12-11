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


class UnionFindVerDepth:
    def __init__(self, n):
        #親要素のノード番号を格納　par[x]==xのときそのノードは根 1からn
        self.par = [i for i in range(n+1)]
        #木の高さを格納
        self.rank = [0] * (n+1)

    def find(self, x):
        #根ならその番号を返す
        if self.par[x] == x:
            return x
        else:
            #親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        #根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        #木の高さを比較し、低いほうから高いほうへつなぐ
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


class UnionFindVerSize:
    def __init__(self, n):
        #親要素のノード番号を格納　par[x]==xのときそのノードは根 1からn
        self.par = [i for i in range(n+1)]
        #木のサイズを格納
        self.size = [1] * (n+1)

    def find(self, x):
        #根ならその番号を返す
        if self.par[x] == x:
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
        if self.size[x] < self.size[y]:
            self.par[x] = y
            self.size[x] += self.size[y]
        else:
            self.par[y] = x
            self.size[y] += self.size[x]

    def get_size(self, x):
        return self.size(self.find(x))

    def get_group_num(self):
        ans = 0
        for i in range(1, len(self.par)):
            if self.find(i) == i:
                ans += 1
        return ans
