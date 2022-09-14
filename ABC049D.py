import sys
from collections import Counter

MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self.group_num = n

    def find(self, x):
        # 根ならその番号を返す
        if self.par[x] < 0:
            return x
        else:
            # 親の親は親
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def is_same(self, x, y):
        # 根が同じならTrue
        return self.find(x) == self.find(y)

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return

        # 木のサイズを比較し、小さいほうから大きいほうへつなぐ
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.group_num -= 1
        self.roots.discard(y)
        assert self.group_num == len(self.roots)


        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return len(self.roots)




def main():
    N, K, L = NMI()
    PQ = [NLI() for _ in range(K)]
    PQ = [[x-1, y-1] for x, y in PQ]
    RS = [NLI() for _ in range(L)]
    RS = [[x-1, y-1] for x, y in RS]

    uf = UnionFind(N)
    for p, q in PQ:
        uf.unite(p, q)

    uf2 = UnionFind(N)
    for r, s in RS:
        uf2.unite(r, s)

    R1 = [uf.find(i) for i in range(N)]
    R2 = [uf2.find(i) for i in range(N)]

    C = Counter([(x, y) for x, y in zip(R1, R2)])
    ans = []
    for x, y in zip(R1, R2):
        ans.append(C[(x, y)])
    print(*ans)


if __name__ == "__main__":
    main()
