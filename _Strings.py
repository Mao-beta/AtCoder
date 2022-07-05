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


# ACL for Python
class string:
    def sa_is(s, upper):
        n=len(s)
        if n==0:
            return []
        if n==1:
            return [0]
        if n==2:
            if (s[0]<s[1]):
                return [0,1]
            else:
                return [1,0]
        sa=[0]*n
        ls=[0]*n
        for i in range(n-2,-1,-1):
            ls[i]=ls[i+1] if (s[i]==s[i+1]) else (s[i]<s[i+1])
        sum_l=[0]*(upper+1)
        sum_s=[0]*(upper+1)
        for i in range(n):
            if not(ls[i]):
                sum_s[s[i]]+=1
            else:
                sum_l[s[i]+1]+=1
        for i in range(upper+1):
            sum_s[i]+=sum_l[i]
            if i<upper:
                sum_l[i+1]+=sum_s[i]
        def induce(lms):
            for i in range(n):
                sa[i]=-1
            buf=sum_s[:]
            for d in lms:
                if d==n:
                    continue
                sa[buf[s[d]]]=d
                buf[s[d]]+=1
            buf=sum_l[:]
            sa[buf[s[n-1]]]=n-1
            buf[s[n-1]]+=1
            for i in range(n):
                v=sa[i]
                if v>=1 and not(ls[v-1]):
                    sa[buf[s[v-1]]]=v-1
                    buf[s[v-1]]+=1
            buf=sum_l[:]
            for i in range(n-1,-1,-1):
                v=sa[i]
                if v>=1 and ls[v-1]:
                    buf[s[v-1]+1]-=1
                    sa[buf[s[v-1]+1]]=v-1
        lms_map=[-1]*(n+1)
        m=0
        for i in range(1,n):
            if not(ls[i-1]) and ls[i]:
                lms_map[i]=m
                m+=1
        lms=[]
        for i in range(1,n):
            if not(ls[i-1]) and ls[i]:
                lms.append(i)
        induce(lms)
        if m:
            sorted_lms=[]
            for v in sa:
                if lms_map[v]!=-1:
                    sorted_lms.append(v)
            rec_s=[0]*m
            rec_upper=0
            rec_s[lms_map[sorted_lms[0]]]=0
            for i in range(1,m):
                l=sorted_lms[i-1]
                r=sorted_lms[i]
                end_l=lms[lms_map[l]+1] if (lms_map[l]+1<m) else n
                end_r=lms[lms_map[r]+1] if (lms_map[r]+1<m) else n
                same=True
                if end_l-l!=end_r-r:
                    same=False
                else:
                    while(l<end_l):
                        if s[l]!=s[r]:
                            break
                        l+=1
                        r+=1
                    if (l==n) or (s[l]!=s[r]):
                        same=False
                if not(same):
                    rec_upper+=1
                rec_s[lms_map[sorted_lms[i]]]=rec_upper
            rec_sa=string.sa_is(rec_s,rec_upper)
            for i in range(m):
                sorted_lms[i]=lms[rec_sa[i]]
            induce(sorted_lms)
        return sa

    def suffix_array_upper(s, upper):
        assert 0<=upper
        for d in s:
            assert 0<=d and d<=upper
        return string.sa_is(s,upper)

    def suffix_array(s):
        n=len(s)
        if type(s)==str:
            s2=[ord(i) for i in s]
            return string.sa_is(s2,255)
        else:
            idx=list(range(n))
            idx.sort(key=lambda x:s[x])
            s2=[0]*n
            now=0
            for i in range(n):
                if (i& s[idx[i-1]]!=s[idx[i]]):
                    now+=1
                s2[idx[i]]=now
            return string.sa_is(s2,now)

    def lcp_array(s, sa):
        """
        lcp-array(Longest Common Prefix)を求めます。
        呼び出す際には事前にsuffix_arrayのリストを持つことが要求されます。
        """
        n=len(s)
        assert n>=1
        rnk=[0]*n
        for i in range(n):
            rnk[sa[i]]=i
        lcp=[0]*(n-1)
        h=0
        for i in range(n):
            if h>0:
                h-=1
            if rnk[i]==0:
                continue
            j=sa[rnk[i]-1]
            while(j+h<n and i+h<n):
                if s[j+h]!=s[i+h]:
                    break
                h+=1
            lcp[rnk[i]-1]=h
        return lcp

    def z_algorithm(s):
        """
        文字列が与えられた時、各 i について
        「S と S[i:] の最長共通接頭辞の長さ」
        を記録した配列 A を O(|S|) で構築する
        """
        n=len(s)
        if n==0:
            return []
        z=[0]*n
        i=1;j=0
        while(i<n):
            z[i]=0 if (j+z[j]<=i) else min(j+z[j]-i,z[i-j])
            while((i+z[i]<n) and (s[z[i]]==s[i+z[i]])):
                z[i]+=1
            if (j+z[j]<i+z[i]):
                j=i
            i+=1
        z[0]=n
        return z


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# RUN LENGTH DECODING list(tuple()) -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L: "list[tuple]") -> str:
    res = ""
    for c, n in L:
        res += c * int(n)
    return res

# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S: str) -> str:
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res



# 編集距離
S = "acpc"
T = "acm"
SL = len(S)
TL = len(T)

@lru_cache(maxsize=None)
def edit_distance(i, j):
    if i >= SL: return TL - j
    if j >= TL: return SL - i
    if S[i] == T[j]:
        return edit_distance(i + 1, j + 1)

    res_add = edit_distance(i, j + 1)
    res_del = edit_distance(i + 1, j)
    res_mod = edit_distance(i + 1, j + 1)
    return 1 + min(res_add, res_del, res_mod)



# KMP法
# 1対1の検索アルゴリズム。Tが固定のときTableを使いまわせる？
# 前計算O(|T|), 検索O(|S|)
# 事前にTから「j文字目で照合失敗したら次は何文字ずらすか」テーブルを作っておき、
# マッチ位置を試す位置を少なくする。
def make_kmp_table(t):
    """
    tbl[i]: t[:x] == t[i-x:i] となる最大のx
    つまり、tのi文字目からみて後ろ何文字が、tのprefixと一致するか
    """
    i = 2
    j = 0
    m = len(t)
    tbl = [0] * (m + 1)
    tbl[0] = -1
    while i <= m:
        if t[i - 1] == t[j]:
            tbl[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = tbl[j]
        else:
            tbl[i] = 0
            i += 1
    return tbl


def kmp(s, t):
    matched_indices = []
    tbl = make_kmp_table(t)
    i = 0
    j = 0
    n = len(s)
    m = len(t)
    while i + j < n:
        if t[j] == s[i + j]:
            j += 1
            if j == m:
                matched_indices.append(i)
                i += j - tbl[j]
                j = tbl[j]
        else:
            i += j - tbl[j]
            if j > 0:
                j = tbl[j]
    return matched_indices



class RollingHash():
    """
    文字列SについてのHash table
    rh = RollingHash(S, 37, MOD)
    hash = rh.get(l, r) # S[l:r]のhash
    """
    def __init__(self, s, base, mod):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)

        l = len(s)
        self.h = h = [0]*(l+1)

        v = 0
        for i in range(l):
            h[i+1] = v = (v * base + ord(s[i])) % mod
        v = 1
        for i in range(l):
            pw[i+1] = v = v * base % mod

    def get(self, l, r):
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod





# 自前ローリングハッシュ用
import random
M = 998244353
b = random.sample(range(10 ** 4, 10 ** 5), 1)[0]

def make_hash(S, b, m):
    # SのHash tableを作る　O(|S|)
    H = [0]
    for s in S:
        H.append((H[-1] * b + s) % m)
    return H

def sub_hash(H, P, M, l, r):
    # Sの累積HashリストHから、部分文字列S[l:r]のhashを計算する
    # Pは基数bのpow、Mは剰余の法
    # 前計算していればO(1)
    return (H[r] - P[r-l] * H[l]) % M


import random
def rabin_karp(s, t):
    """
    ローリングハッシュ
    ハッシュ化にO(|S|+|T|)、検索にO(|S|)
    sの連続部分文字列でtに一致するものの始点のindexをまとめてlistで返す
    """
    def exe(x, m):
        th = 0
        for c in tt:
            th = (th * x + c) % m

        sh = 0
        for c in st[:l]:
            sh = (sh * x + c) % m
        xl = pow(x, l - 1, m)

        matched = set()
        if sh == th:
            matched.add(0)
        for i, (c0, c1) in enumerate(zip(st, st[l:]), start=1):
            sh = ((sh - c0 * xl) * x + c1) % m
            if sh == th:
                matched.add(i)

        return matched

    l = len(t)
    st = list(map(ord, s))
    tt = list(map(ord, t))
    # Xはなるべくst,ttの最大要素より大きくする
    # Mはとりあえず2^61-1(素数)を設定する
    xs = random.sample(range(10 ** 9, 10 ** 10), 3)
    ans = exe(xs[0], 2305843009213693951)
    ans.intersection_update(exe(xs[1], 2305843009213693951))
    ans.intersection_update(exe(xs[2], 2305843009213693951))
    return sorted(ans)


def manacher(s):
    """
    文字列Sから奇数長の最長の回文をO(|S|)で検索するアルゴリズム。
    Sの各文字の間にSには絶対に登場しないダミー文字を挟み込むと、偶数長の回文も見つけられる。
    両端と各文字の間に'$'を挿入すると、「各要素の値-1」がそこを中心とした回文の長さとなる。
    """
    n = len(s)
    radius = [0] * n
    i, j = 0, 0
    while i < n:
        while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
            j += 1
        radius[i] = j
        k = 1
        while i - k >= 0 and i + k < n and k + radius[i - k] < j:
            radius[i + k] = radius[i - k]
            k += 1
        i += k
        j -= k
    return radius



def main():
    S = input()
    T = input()
    ans = kmp(S, T)
    print(*ans, end="\n")


if __name__ == "__main__":
    main()