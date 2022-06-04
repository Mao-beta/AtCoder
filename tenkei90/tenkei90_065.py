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


class Comb:
    """nCrのnもrも10**7くらいまで"""

    def __init__(self, n, mod):
        self.mod = mod
        self.fac = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        for i in range(1, n + 1):
            self.fac[i] = self.fac[i - 1] * i % self.mod
        self.inv[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n - 1, 0, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod

    def C(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod

    def P(self, n, r):
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * self.inv[n - r] % self.mod

    def H(self, n, r):
        return self.C(n + r - 1, r - 1)


class FFT():
    def primitive_root_constexpr(self,m):
        if m==2:return 1
        if m==167772161:return 3
        if m==469762049:return 3
        if m==754974721:return 11
        if m==998244353:return 3
        divs=[0]*20
        divs[0]=2
        cnt=1
        x=(m-1)//2
        while(x%2==0):x//=2
        i=3
        while(i*i<=x):
            if (x%i==0):
                divs[cnt]=i
                cnt+=1
                while(x%i==0):
                    x//=i
            i+=2
        if x>1:
            divs[cnt]=x
            cnt+=1
        g=2
        while(1):
            ok=True
            for i in range(cnt):
                if pow(g,(m-1)//divs[i],m)==1:
                    ok=False
                    break
            if ok:
                return g
            g+=1
    def bsf(self,x):
        res=0
        while(x%2==0):
            res+=1
            x//=2
        return res
    butterfly_first=True
    butterfly_inv_first=True
    sum_e=[0]*30
    sum_ie=[0]*30
    def __init__(self,MOD):
        self.mod=MOD
        self.g=self.primitive_root_constexpr(self.mod)
    def butterfly(self,a):
        n=len(a)
        h=(n-1).bit_length()
        if self.butterfly_first:
            self.butterfly_first=False
            es=[0]*30
            ies=[0]*30
            cnt2=self.bsf(self.mod-1)
            e=pow(self.g,(self.mod-1)>>cnt2,self.mod)
            ie=pow(e,self.mod-2,self.mod)
            for i in range(cnt2,1,-1):
                es[i-2]=e
                ies[i-2]=ie
                e=(e*e)%self.mod
                ie=(ie*ie)%self.mod
            now=1
            for i in range(cnt2-2):
                self.sum_e[i]=((es[i]*now)%self.mod)
                now*=ies[i]
                now%=self.mod
        for ph in range(1,h+1):
            w=1<<(ph-1)
            p=1<<(h-ph)
            now=1
            for s in range(w):
                offset=s<<(h-ph+1)
                for i in range(p):
                    l=a[i+offset]
                    r=a[i+offset+p]*now
                    r%=self.mod
                    a[i+offset]=l+r
                    a[i+offset]%=self.mod
                    a[i+offset+p]=l-r
                    a[i+offset+p]%=self.mod
                now*=self.sum_e[(~s & -~s).bit_length()-1]
                now%=self.mod
    def butterfly_inv(self,a):
        n=len(a)
        h=(n-1).bit_length()
        if self.butterfly_inv_first:
            self.butterfly_inv_first=False
            es=[0]*30
            ies=[0]*30
            cnt2=self.bsf(self.mod-1)
            e=pow(self.g,(self.mod-1)>>cnt2,self.mod)
            ie=pow(e,self.mod-2,self.mod)
            for i in range(cnt2,1,-1):
                es[i-2]=e
                ies[i-2]=ie
                e=(e*e)%self.mod
                ie=(ie*ie)%self.mod
            now=1
            for i in range(cnt2-2):
                self.sum_ie[i]=((ies[i]*now)%self.mod)
                now*=es[i]
                now%=self.mod
        for ph in range(h,0,-1):
            w=1<<(ph-1)
            p=1<<(h-ph)
            inow=1
            for s in range(w):
                offset=s<<(h-ph+1)
                for i in range(p):
                    l=a[i+offset]
                    r=a[i+offset+p]
                    a[i+offset]=l+r
                    a[i+offset]%=self.mod
                    a[i+offset+p]=(l-r)*inow
                    a[i+offset+p]%=self.mod
                inow*=self.sum_ie[(~s & -~s).bit_length()-1]
                inow%=self.mod
    def convolution(self,a,b):
        n=len(a);m=len(b)
        if not(a) or not(b):
            return []
        if min(n,m)<=40:
            if n<m:
                n,m=m,n
                a,b=b,a
            res=[0]*(n+m-1)
            for i in range(n):
                for j in range(m):
                    res[i+j]+=a[i]*b[j]
                    res[i+j]%=self.mod
            return res
        z=1<<((n+m-2).bit_length())
        a=a+[0]*(z-n)
        b=b+[0]*(z-m)
        self.butterfly(a)
        self.butterfly(b)
        c=[0]*z
        for i in range(z):
            c[i]=(a[i]*b[i])%self.mod
        self.butterfly_inv(c)
        iz=pow(z,self.mod-2,self.mod)
        for i in range(n+m-1):
            c[i]=(c[i]*iz)%self.mod
        return c[:n+m-1]


def main():
    R, G, B, K = NMI()
    X, Y, Z = NMI()

    R2 = max(0, K - Y)
    G2 = max(0, K - Z)
    B2 = max(0, K - X)

    C = Comb(R+G+B+1, MOD99)

    # 赤をR2個以上、緑をG2個以上、青をB2個以上選ぶ
    if R2 + G2 + B2 > K:
        print(0)
        exit()
    if R2 > R or G2 > G or B2 > B:
        print(0)
        exit()

    Conv = FFT(MOD99)

    RF = [0] * (R+1)
    GF = [0] * (G+1)
    BF = [0] * (B+1)

    for r in range(R2, R+1):
        RF[r] = C.C(R, r)

    for g in range(G2, G+1):
        GF[g] = C.C(G, g)

    for b in range(B2, B+1):
        BF[b] = C.C(B, b)

    X = Conv.convolution(RF, GF)[:K+1]
    ans = Conv.convolution(X, BF)
    print(ans[K])


if __name__ == "__main__":
    main()
