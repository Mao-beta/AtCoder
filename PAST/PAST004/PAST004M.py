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
EI = lambda m: [NLI() for _ in range(m)]


class HeavyLightDecomposition:
    def __init__(self, n, G):
        """
        HL分解（Heavy-Light Decomposition）
        木構造上のパスや部分木に対するクエリを、複数のセグメント木や平衡二分木に分割し、
        それぞれのデータ構造を使って高速にクエリを処理することができる。
        木を「重い辺」(heavy edge)と「軽い辺」(light edge)に分割し、木の各頂点が最大1つの重い辺を持つようになる。
        そして、各重い辺から成るパスを分割し、それぞれのパスに対してデータ構造を構築する。
        :param n: 頂点数
        :param G: 隣接リスト(0-index)

        .order[i]: iをDFS行きがけ順に変換したときのorder
        """
        self.n = n
        self.sub_size = [1] * n
        self.par = [-1] * n

        todo = [0]
        while todo:
            v = todo.pop()
            if v >= 0:
                for u in G[v]:
                    if u != self.par[v]:
                        todo.append(~u)
                        todo.append(u)
                        self.par[u] = v
            else:
                v = ~v
                self.sub_size[self.par[v]] += self.sub_size[v]

        self.head = [-1] * n
        self.head[0] = 0
        self.order = [-1] * n
        self.heavy_child = [-1] * n
        self.inv_order = [-1] * n

        todo = [0]
        cnt = 0
        while todo:
            v = todo.pop()
            self.order[v] = cnt
            self.inv_order[cnt] = v
            cnt += 1
            mx = 0
            for u in G[v]:
                if u != self.par[v] and mx < self.sub_size[u]:
                    mx = self.sub_size[u]
                    self.heavy_child[v] = u
            for u in G[v]:
                if self.par[v] != u and self.heavy_child[v] != u:
                    self.head[u] = u
                    todo.append(u)
            if self.heavy_child[v] != -1:
                self.head[self.heavy_child[v]] = self.head[v]
                todo.append(self.heavy_child[v])

    def for_each_edge(self, u, v):
        """
        頂点uから頂点vまでの各辺に対して区間クエリを行いたいときの、[l, r)のリスト
        これらをseg.prodなどにつっこむ
        """
        paths = []
        while True:
            if self.order[u] > self.order[v]:
                u, v = v, u
            if self.head[u] != self.head[v]:
                paths.append((self.order[self.head[v]], self.order[v] + 1))
                v = self.par[self.head[v]]
            else:
                paths.append((self.order[u] + 1, self.order[v] + 1))
                return paths

    def for_each_vertex(self, u, v):
        """
        頂点uから頂点vまでの各頂点に対して区間クエリを行いたいときの、[l, r)のリスト
        これらをseg.prodなどにつっこむ
        """
        paths = []
        while True:
            if self.order[u] > self.order[v]:
                u, v = v, u
            if self.head[u] != self.head[v]:
                paths.append((self.order[self.head[v]], self.order[v] + 1))
                v = self.par[self.head[v]]
            else:
                paths.append((self.order[u], self.order[v] + 1))
                return paths


def adjlist(n, edges, directed=False, in_origin=1):
    if len(edges) == 0:
        return [[] for _ in range(n)]

    weighted = True if len(edges[0]) > 2 else False
    if in_origin == 1:
        if weighted:
            edges = [[x-1, y-1, w] for x, y, w in edges]
        else:
            edges = [[x-1, y-1] for x, y in edges]

    res = [[] for _ in range(n)]

    if weighted:
        for u, v, c in edges:
            res[u].append([v, c])
            if not directed:
                res[v].append([u, c])

    else:
        for u, v in edges:
            res[u].append(v)
            if not directed:
                res[v].append(u)

    return res


class lazy_segtree():
    def update(self,k):self.d[k]=self.op(self.d[2*k],self.d[2*k+1])

    def all_apply(self,k,f):
        self.d[k]=self.mapping(f,self.d[k])
        if (k<self.size):self.lz[k]=self.composition(f,self.lz[k])

    def push(self,k):
        self.all_apply(2*k,self.lz[k])
        self.all_apply(2*k+1,self.lz[k])
        self.lz[k]=self.identity

    def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):
        self.n=len(V)
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        self.lz=[ID for i in range(self.size)]
        self.e=E
        self.op=OP
        self.mapping=MAPPING
        self.composition=COMPOSITION
        self.identity=ID
        for i in range(self.n):self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):self.update(i)

    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=x
        for i in range(1,self.log+1):self.update(p>>i)

    def get(self,p):
        assert 0<=p and p<self.n
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        return self.d[p]

    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        if l==r:return self.e
        l+=self.size
        r+=self.size
        for i in range(self.log,0,-1):
            if (((l>>i)<<i)!=l):self.push(l>>i)
            if (((r>>i)<<i)!=r):self.push(r>>i)
        sml,smr=self.e,self.e
        while(l<r):
            if l&1:
                sml=self.op(sml,self.d[l])
                l+=1
            if r&1:
                r-=1
                smr=self.op(self.d[r],smr)
            l>>=1
            r>>=1
        return self.op(sml,smr)

    def all_prod(self):return self.d[1]

    def apply_point(self,p,f):
        assert 0<=p and p<self.n
        p+=self.size
        for i in range(self.log,0,-1):self.push(p>>i)
        self.d[p]=self.mapping(f,self.d[p])
        for i in range(1,self.log+1):self.update(p>>i)

    def apply(self,l,r,f):
        assert 0<=l and l<=r and r<=self.n
        if l==r:return
        l+=self.size
        r+=self.size
        for i in range(self.log,0,-1):
            if (((l>>i)<<i)!=l):self.push(l>>i)
            if (((r>>i)<<i)!=r):self.push((r-1)>>i)
        l2,r2=l,r
        while(l<r):
            if (l&1):
                self.all_apply(l,f)
                l+=1
            if (r&1):
                r-=1
                self.all_apply(r,f)
            l>>=1
            r>>=1
        l,r=l2,r2
        for i in range(1,self.log+1):
            if (((l>>i)<<i)!=l):self.update(l>>i)
            if (((r>>i)<<i)!=r):self.update((r-1)>>i)

    def max_right(self,l,g):
        assert 0<=l and l<=self.n
        assert g(self.e)
        if l==self.n:return self.n
        l+=self.size
        for i in range(self.log,0,-1):self.push(l>>i)
        sm=self.e
        while(1):
            while(l%2==0):l>>=1
            if not(g(self.op(sm,self.d[l]))):
                while(l<self.size):
                    self.push(l)
                    l=(2*l)
                    if (g(self.op(sm,self.d[l]))):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:break
        return self.n

    def min_left(self,r,g):
        assert (0<=r and r<=self.n)
        assert g(self.e)
        if r==0:return 0
        r+=self.size
        for i in range(self.log,0,-1):self.push((r-1)>>i)
        sm=self.e
        while(1):
            r-=1
            while(r>1 and (r%2)):r>>=1
            if not(g(self.op(self.d[r],sm))):
                while(r<self.size):
                    self.push(r)
                    r=(2*r+1)
                    if g(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r&-r)==r:break
        return 0


# 区間min取得(prod)・区間更新(apply)
INF = 1<<60
# opの恒等写像
E = INF

def op(s, t):
    return min(s, t)

def mapping(f, a):
    # f: 作用する、a: 作用される
    if f == ID:
        return a
    return f

def composition(f, g):
    # f(g())
    return g if f == ID else f

# mappingの単位元
ID = -1


def main():
    N, Q = NMI()
    AB = EI(N-1)
    UVC = EI(Q)
    G = adjlist(N, AB)
    hld = HeavyLightDecomposition(N, G)
    seg = lazy_segtree([0]*N, op, E, mapping, composition, ID)
    for u, v, c in UVC:
        u, v = u-1, v-1
        lrs = hld.for_each_edge(u, v)
        for l, r in lrs:
            seg.apply(l, r, c)

    for a, b in AB:
        a, b = a-1, b-1
        lrs = hld.for_each_edge(a, b)
        for l, r in lrs:
            # print("#", l, r)
            if l != r:
                print(seg.prod(l, r))


if __name__ == "__main__":
    main()
