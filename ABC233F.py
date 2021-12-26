import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納　xが根のとき-(サイズ)を格納
        self.par = [-1 for i in range(n)]
        self.n = n
        self.roots = set(range(n))
        self._group_num = n
        self.members = defaultdict(set)

        for i in range(n):
            self.members[i].add(i)

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

        self._group_num -= 1
        self.roots.discard(y)
        assert self._group_num == len(self.roots)

        self.members[x] |= self.members[y]
        del self.members[y]

        self.par[x] += self.par[y]
        self.par[y] = x

    def size(self, x):
        return -self.par[self.find(x)]

    def get_members(self, x):
        root = self.find(x)
        return self.members[root]

    def get_roots(self):
        return self.roots

    def group_count(self):
        return self._group_num

    def all_group_members(self):
        return self.members

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members[r]) for r in self.roots)


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N = NI()
    P = NLI()
    P = [x-1 for x in P]
    M = NI()
    AB = [NLI() for _ in range(M)]
    adj = adjlist_nond_1to0(N, AB)
    AB = [[x-1, y-1] for x, y in AB]
    AB_to_idx = {(a, b): i for i, (a, b) in enumerate(AB)}


    # 連結成分ごとに木を構築
    forest = [[] for _ in range(N)]
    sub_uf = UnionFind(N)

    for m in range(N):
        for goto in adj[m]:
            if sub_uf.is_same(m, goto):
                continue
            sub_uf.unite(m, goto)
            forest[m].append(goto)
            forest[goto].append(m)


    # 葉からの順番を取得
    seen = [0] * N
    order = []

    def dfs(now):
        for goto in forest[now]:
            if seen[goto]: continue
            seen[goto] = 1
            dfs(goto)
        order.append(now)

    for start in range(N):
        seen[start] = 1
        dfs(start)

    assert set(order) == set(P)
    #print(order)

    # 頂点iに駒iを持ってくる作業をorder順にやる
    Q = P[:]

    ans = []

    # 頂点nowに駒targetを持ってくる
    # targetのある頂点をreturnし、呼び出し元でswap...を繰り返す
    # 先にtargetの無い頂点ではNoneを返す
    def bring(now, target):
        seen[now] = 1

        if Q[now] == target:
            return now

        # print("in", now, Q[now])

        v = None
        for goto in forest[now]:
            if seen[goto]:
                continue
            # print("now, goto", now, goto)
            v = bring(goto, target)
            # print(v)
            if v is not None:
                # 見つけたら抜ける
                break

        # print("out", now, Q[now], v)
        if v is not None:
            # swap
            Q[now], Q[v] = Q[v], Q[now]
            # print("swap", Q[now], Q[v], Q)
            # 出力する捜査の番号を保存
            a, b = min(now, v), max(now, v)
            assert (a, b) in AB_to_idx.keys()
            assert Q[now] == target
            ans.append(AB_to_idx[(a, b)] + 1)
            # いまtargetはnowにあるので返す
            return now

        else:
            # targetは見つからなかった
            return

    # print("base", Q)
    for goal in order:
        # print("bring start", goal+1)
        seen = [0] * N
        v = bring(goal, goal)
        # print(goal, v)
        # print(Q)

    assert len(ans) <= 500000
    # print(Q)
    # print(order)
    if list(range(N)) != Q:
        print(-1)
    else:
        print(len(ans))
        print(*ans)


if __name__ == "__main__":
    main()
