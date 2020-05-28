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
