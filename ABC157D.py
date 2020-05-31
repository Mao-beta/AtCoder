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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M, K = map(int, input().split())
graph = [set() for _ in range(N)]
block = [set() for _ in range(N)]
union = UnionFind(N)
for i in range(M):
    a, b = map(int, input().split())
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)
    union.unite(a-1, b-1)
for i in range(K):
    a, b = map(int, input().split())
    block[a-1].add(b-1)
    block[b-1].add(a-1)

blocking = [0] * N
for i, blo in enumerate(block):
    for b in blo:
        if union.is_same(i, b):
            blocking[i] += 1

for i in range(N):
    ans = union.size(i) - len(graph[i]) - blocking[i] - 1
    print(ans)
