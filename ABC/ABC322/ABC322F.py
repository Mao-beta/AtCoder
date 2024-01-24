import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


# class lazy_segtree():
#     def update(self,k):self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
#
#     def all_apply(self,k,f):
#         self.d[k]=self.mapping(f,self.d[k])
#         if (k<self.size):self.lz[k]=self.composition(f,self.lz[k])
#
#     def push(self,k):
#         self.all_apply(2*k,self.lz[k])
#         self.all_apply(2*k+1,self.lz[k])
#         self.lz[k]=self.identity
#
#     def __init__(self,V,OP,E,MAPPING,COMPOSITION,ID):
#         self.n=len(V)
#         self.log=(self.n-1).bit_length()
#         self.size=1<<self.log
#         self.d=[E for i in range(2*self.size)]
#         self.lz=[ID for i in range(self.size)]
#         self.e=E
#         self.op=OP
#         self.mapping=MAPPING
#         self.composition=COMPOSITION
#         self.identity=ID
#         for i in range(self.n):self.d[self.size+i]=V[i]
#         for i in range(self.size-1,0,-1):self.update(i)
#
#     def set(self,p,x):
#         assert 0<=p and p<self.n
#         p+=self.size
#         for i in range(self.log,0,-1):self.push(p>>i)
#         self.d[p]=x
#         for i in range(1,self.log+1):self.update(p>>i)
#
#     def get(self,p):
#         assert 0<=p and p<self.n
#         p+=self.size
#         for i in range(self.log,0,-1):self.push(p>>i)
#         return self.d[p]
#
#     def prod(self,l,r):
#         assert 0<=l and l<=r and r<=self.n
#         if l==r:return self.e
#         l+=self.size
#         r+=self.size
#         for i in range(self.log,0,-1):
#             if (((l>>i)<<i)!=l):self.push(l>>i)
#             if (((r>>i)<<i)!=r):self.push(r>>i)
#         sml,smr=self.e,self.e
#         while(l<r):
#             if l&1:
#                 sml=self.op(sml,self.d[l])
#                 l+=1
#             if r&1:
#                 r-=1
#                 smr=self.op(self.d[r],smr)
#             l>>=1
#             r>>=1
#         return self.op(sml,smr)
#
#     def all_prod(self):return self.d[1]
#
#     def apply_point(self,p,f):
#         assert 0<=p and p<self.n
#         p+=self.size
#         for i in range(self.log,0,-1):self.push(p>>i)
#         self.d[p]=self.mapping(f,self.d[p])
#         for i in range(1,self.log+1):self.update(p>>i)
#
#     def apply(self,l,r,f):
#         assert 0<=l and l<=r and r<=self.n
#         if l==r:return
#         l+=self.size
#         r+=self.size
#         for i in range(self.log,0,-1):
#             if (((l>>i)<<i)!=l):self.push(l>>i)
#             if (((r>>i)<<i)!=r):self.push((r-1)>>i)
#         l2,r2=l,r
#         while(l<r):
#             if (l&1):
#                 self.all_apply(l,f)
#                 l+=1
#             if (r&1):
#                 r-=1
#                 self.all_apply(r,f)
#             l>>=1
#             r>>=1
#         l,r=l2,r2
#         for i in range(1,self.log+1):
#             if (((l>>i)<<i)!=l):self.update(l>>i)
#             if (((r>>i)<<i)!=r):self.update((r-1)>>i)
#
#     def max_right(self,l,g):
#         """
#         0≤l<Nなる整数 l および条件式 f が与えられたとき、
#         f(prod(l,r))=True となる最大の r を求める。
#         ただし、与えられる条件式 f は次を満たす:
#         ある整数 x>l に対し、f(prod(l,x))=True であるとき、
#         任意の整数 l<y≤x について f(prod(l,y))=True である。また、f(e)=True である。
#         ->lから右にprodを伸ばしていくとき、はじめて条件がFalseになるrをさがす
#         """
#         assert 0<=l and l<=self.n
#         assert g(self.e)
#         if l==self.n:return self.n
#         l+=self.size
#         for i in range(self.log,0,-1):self.push(l>>i)
#         sm=self.e
#         while(1):
#             while(l%2==0):l>>=1
#             if not(g(self.op(sm,self.d[l]))):
#                 while(l<self.size):
#                     self.push(l)
#                     l=(2*l)
#                     if (g(self.op(sm,self.d[l]))):
#                         sm=self.op(sm,self.d[l])
#                         l+=1
#                 return l-self.size
#             sm=self.op(sm,self.d[l])
#             l+=1
#             if (l&-l)==l:break
#         return self.n
#
#     def min_left(self,r,g):
#         """
#         0≤r<Nなる整数 r および条件式 f が与えられたとき、
#         f(prod(l,r))=True となる最小の l を求める。
#         ただし、与えられる条件式 f は次を満たす:
#         ある整数 x<r に対し、f(prod(x,r))=True であるとき、
#         任意の整数 x≤y<r について f(prod(y,r))=True である。また、f(e)=True である。
#         ->rから左にprodを伸ばしていくとき、はじめて条件がFalseになるlをさがす
#         """
#         assert (0<=r and r<=self.n)
#         assert g(self.e)
#         if r==0:return 0
#         r+=self.size
#         for i in range(self.log,0,-1):self.push((r-1)>>i)
#         sm=self.e
#         while(1):
#             r-=1
#             while(r>1 and (r%2)):r>>=1
#             if not(g(self.op(self.d[r],sm))):
#                 while(r<self.size):
#                     self.push(r)
#                     r=(2*r+1)
#                     if g(self.op(self.d[r],sm)):
#                         sm=self.op(self.d[r],sm)
#                         r-=1
#                 return r+1-self.size
#             sm=self.op(self.d[r],sm)
#             if (r&-r)==r:break
#         return 0

class LazySegTree:
    def __init__(self, v, op, e, mapping, composition, id_):
        n = len(v)
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_
        self._size = 1 << (n - 1).bit_length()
        self._d = [e] * (2 * self._size)
        self._lz = [id_] * 2 * self._size
        for i in range(n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._d[i] = self._op(self._d[2 * i], self._d[2 * i + 1])

    def _gindex(self, l, r):
        l += self._size
        r += self._size
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            l >>= 1
            r >>= 1
        while l:
            yield l
            l >>= 1

    def _propagates(self, *ids):
        for i in reversed(ids):
            f = self._lz[i]
            self._lz[i] = self._id
            self._lz[2 * i] = self._composition(f, self._lz[2 * i])
            self._lz[2 * i + 1] = self._composition(f, self._lz[2 * i + 1])
            self._d[2 * i] = self._mapping(f, self._d[2 * i])
            self._d[2 * i + 1] = self._mapping(f, self._d[2 * i + 1])

    def apply(self, l, r, f):
        (*ids,) = self._gindex(l, r)
        self._propagates(*ids)
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                self._lz[l] = self._composition(f, self._lz[l])
                self._d[l] = self._mapping(f, self._d[l])
                l += 1
            if r & 1:
                self._lz[r - 1] = self._composition(f, self._lz[r - 1])
                self._d[r - 1] = self._mapping(f, self._d[r - 1])
            l >>= 1
            r >>= 1
        for i in ids:
            self._d[i] = self._op(self._d[2 * i], self._d[2 * i + 1])

    def prod(self, l, r):
        self._propagates(*self._gindex(l, r))
        resl = self._e
        resr = self._e
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                resl = self._op(resl, self._d[l])
                l += 1
            if r & 1:
                resr = self._op(self._d[r - 1], resr)
            l >>= 1
            r >>= 1
        return self._op(resl, resr)


# 区間和・個数取得(prod)・区間affine変換(apply)
INF = 1<<60
# keta = 20

# def func(m, l, r):
#     return (m << (keta*2)) | (l << keta) | r


MASK = (1 << 20) - 1

# def inv(x):
#     m = x >> 40
#     l = (x >> 20) & MASK
#     r = x & MASK
#     return m, l, r

def op(X, Y):
    xm = X[0] >> 40
    xl = (X[0] >> 20) & MASK
    xr = X[0] & MASK
    xm0 = X[1] >> 40
    xl0 = (X[1] >> 20) & MASK
    xr0 = X[1] & MASK
    ym = Y[0] >> 40
    yl = (Y[0] >> 20) & MASK
    yr = Y[0] & MASK
    ym0 = Y[1] >> 40
    yl0 = (Y[1] >> 20) & MASK
    yr0 = Y[1] & MASK

    m = max(xm, ym, xr + yl)
    m0 = max(xm0, ym0, xr0 + yl0)
    l = xl if xm0 else xl + yl
    r = yr if ym0 else yr + xr
    l0 = xl0 if xm else xl0 + yl0
    r0 = yr0 if ym else yr0 + xr0
    return (m << 40) | (l << 20) | r, (m0 << 40) | (l0 << 20) | r0


# opの単位元
E = (0, 0)


def mapping(f, a):
    # f: 作用する、a: 作用される
    if f:
        return a[1], a[0]
    else:
        return a


def composition(f, g):
    # f(g())
    return f^g


# mappingの単位元
ID = 0


def main():
    N, Q = NMI()
    t = (1 << (20 * 2)) | (1 << 20) | 1
    one = (t, 0)
    zero = (0, t)
    S = [one if s == "1" else zero for s in SI()]
    seg = LazySegTree(S, op, (0, 0), mapping, composition, 0)

    for _ in range(Q):
        c, L, R = NMI()
        L -= 1
        if c == 1:
            seg.apply(L, R, 1)
        else:
            X = seg.prod(L, R)
            xm = X[0] >> 40
            print(xm)


if __name__ == "__main__":
    main()
