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


# // Segment Tree Beats
# // - l<=i<r について、 A_i の値を min(A_i, x) に更新
# // - l<=i<r について、 A_i の値を max(A_i, x) に更新
# // - l<=i<r の中の A_i の最大値を求める
# // - l<=i<r の中の A_i の最小値を求める
# // - l<=i<r の A_i の和を求める
# // - l<=i<r について、 A_i の値に x を加える
# // - l<=i<r について、 A_i の値を x に更新

class SegmentTreeBeats:
    def __init__(self, n, a=None):
        self.inf = 10**18
        self.max_v = [0] * (4 * n)
        self.smax_v = [0] * (4 * n)
        self.max_c = [0] * (4 * n)
        self.min_v = [0] * (4 * n)
        self.smin_v = [0] * (4 * n)
        self.min_c = [0] * (4 * n)
        self.len = [0] * (4 * n)
        self.sum = [0] * (4 * n)
        self.ladd = [0] * (4 * n)
        self.lval = [0] * (4 * n)
        self.n = n
        self.n0 = 1

        while (self.n0 < self.n):
            self.n0 <<= 1

        for i in range(2*self.n0):
            self.ladd[i] = 0
            self.lval[i] = self.inf
        self.len[0] = self.n0
        for i in range(self.n0-1):
            self.len[2 * i + 1] = self.len[2 * i+2] = (self.len[i] >> 1)

        for i in range(n):
            aa = a[i] if a is not None else 0
            self.max_v[self.n0 - 1 + i] = self.min_v[self.n0-1+i] = self.sum[self.n0-1+i] = aa
            self.smax_v[self.n0 - 1 + i] = -self.inf
            self.smin_v[self.n0 - 1 + i] = self.inf
            self.max_c[self.n0 - 1 + i] = self.min_c[self.n0 - 1 + i] = 1

        for i in range(self.n, self.n0):
            self.max_v[self.n0 - 1 + i] = self.smax_v[self.n0-1+i] = -self.inf
            self.min_v[self.n0-1+i] = self.smin_v[self.n0-1+i] = self.inf
            self.max_c[self.n0-1+i] = self.min_c[self.n0-1+i] = 0

        for i in range(self.n0-2, -1, -1):
            self.update(i)


    def update_node_max(self, k, x):
        self.sum[k] += (x - self.max_v[k]) * self.max_c[k]

        if(self.max_v[k] == self.min_v[k]):
            self.max_v[k] = self.min_v[k] = x
        elif(self.max_v[k] == self.smin_v[k]):
            self.max_v[k] = self.smin_v[k] = x
        else:
            self.max_v[k] = x

        if(self.lval[k] != self.inf and x < self.lval[k]):
            self.lval[k] = x


    def update_node_min(self, k, x):
        self.sum[k] += (x - self.min_v[k]) * self.min_c[k]

        if (self.max_v[k] == self.min_v[k]):
            self.max_v[k] = self.min_v[k] = x
        elif (self.smax_v[k] == self.min_v[k]):
            self.min_v[k] = self.smax_v[k] = x
        else:
            self.min_v[k] = x

        if (self.lval[k] != self.inf and self.lval[k] < x):
            self.lval[k] = x


    def push(self, k):

        if(self.n0-1 <= k): return

        if(self.lval[k] != self.inf):
            self.updateall(2*k+1, self.lval[k])
            self.updateall(2*k+2, self.lval[k])
            self.lval[k] = self.inf
            return

        if(self.ladd[k] != 0):
            self.addall(2*k+1, self.ladd[k])
            self.addall(2*k+2, self.ladd[k])
            self.ladd[k] = 0

        if(self.max_v[k] < self.max_v[2*k+1]):
            self.update_node_max(2*k+1, self.max_v[k])

        if(self.min_v[2*k+1] < self.min_v[k]):
            self.update_node_min(2*k+1, self.min_v[k])


        if(self.max_v[k] < self.max_v[2*k+2]):
            self.update_node_max(2*k+2, self.max_v[k])

        if(self.min_v[2*k+2] < self.min_v[k]):
            self.update_node_min(2*k+2, self.min_v[k])



    def update(self, k):
        self.sum[k] = self.sum[2*k+1] + self.sum[2*k+2]

        if(self.max_v[2*k+1] < self.max_v[2*k+2]):
            self.max_v[k] = self.max_v[2*k+2]
            self.max_c[k] = self.max_c[2*k+2]
            self.smax_v[k] = max(self.max_v[2*k+1], self.smax_v[2*k+2])
        elif(self.max_v[2*k+1] > self.max_v[2*k+2]):
            self.max_v[k] = self.max_v[2*k+1]
            self.max_c[k] = self.max_c[2*k+1]
            self.smax_v[k] = max(self.smax_v[2*k+1], self.max_v[2*k+2])
        else:
            self.max_v[k] = self.max_v[2*k+1]
            self.max_c[k] = self.max_c[2*k+1] + self.max_c[2*k+2]
            self.smax_v[k] = max(self.smax_v[2*k+1], self.smax_v[2*k+2])


        if(self.min_v[2*k+1] < self.min_v[2*k+2]):
            self.min_v[k] = self.min_v[2*k+1]
            self.min_c[k] = self.min_c[2*k+1]
            self.smin_v[k] = min(self.smin_v[2*k+1], self.min_v[2*k+2])
        elif(self.min_v[2*k+1] > self.min_v[2*k+2]):
            self.min_v[k] = self.min_v[2*k+2]
            self.min_c[k] = self.min_c[2*k+2]
            self.smin_v[k] = min(self.min_v[2*k+1], self.smin_v[2*k+2])
        else:
            self.min_v[k] = self.min_v[2*k+1]
            self.min_c[k] = self.min_c[2*k+1] + self.min_c[2*k+2]
            self.smin_v[k] = min(self.smin_v[2*k+1], self.smin_v[2*k+2])



    def _update_min(self, x, a, b, k, l, r):
        if(b <= l or r <= a or self.max_v[k] <= x):
            return

        if(a <= l and r <= b and self.smax_v[k] < x):
            self.update_node_max(k, x)
            return

        self.push(k)
        self._update_min(x, a, b, 2*k+1, l, (l+r)//2)
        self._update_min(x, a, b, 2*k+2, (l+r)//2, r)
        self.update(k)

    def _update_max(self, x, a, b, k, l, r):
        if (b <= l or r <= a or x <= self.min_v[k]):
            return

        if (a <= l and r <= b and x < self.smax_v[k]):
            self.update_node_min(k, x)
            return

        self.push(k)
        self._update_max(x, a, b, 2 * k + 1, l, (l + r) // 2)
        self._update_max(x, a, b, 2 * k + 2, (l + r) // 2, r)
        self.update(k)


    def addall(self, k, x):
        self.max_v[k] += x
        if(self.smax_v[k] != -self.inf): self.smax_v[k] += x
        self.min_v[k] += x
        if(self.smin_v[k] != self.inf): self.smin_v[k] += x;

        self.sum[k] += self.len[k] * x
        if(self.lval[k] != self.inf):
            self.lval[k] += x
        else:
            self.ladd[k] += x


    def updateall(self, k, x):
        self.max_v[k] = x
        self.smax_v[k] = -self.inf
        self.min_v[k] = x
        self.smin_v[k] = self.inf
        self.max_c[k] = self.min_c[k] = self.len[k]

        self.sum[k] = x * self.len[k]
        self.lval[k] = x
        self.ladd[k] = 0


    def _add_val(self, x, a, b, k, l, r):
        if(b <= l or r <= a):
            return

        if(a <= l and r <= b):
            self.addall(k, x)
            return


        self.push(k)
        self._add_val(x, a, b, 2*k+1, l, (l+r)//2)
        self._add_val(x, a, b, 2*k+2, (l+r)//2, r)
        self.update(k)


    def _update_val(self, x, a, b, k, l, r):
        if(b <= l or r <= a):
            return

        if(a <= l and r <= b):
            self.updateall(k, x)
            return


        self.push(k)
        self._update_val(x, a, b, 2*k+1, l, (l+r)//2)
        self._update_val(x, a, b, 2*k+2, (l+r)//2, r)
        self.update(k)


    def _query_max(self, a, b, k, l, r):
        if(b <= l or r <= a):
            return -self.inf

        if(a <= l and r <= b):
            return self.max_v[k]

        self.push(k)
        lv = self._query_max(a, b, 2*k+1, l, (l+r)//2)
        rv = self._query_max(a, b, 2*k+2, (l+r)//2, r)
        return max(lv, rv)

    def _query_min(self, a, b, k, l, r):
        if (b <= l or r <= a):
            return self.inf

        if (a <= l and r <= b):
            return self.min_v[k]

        self.push(k)
        lv = self._query_min(a, b, 2 * k + 1, l, (l + r) // 2)
        rv = self._query_min(a, b, 2 * k + 2, (l + r) // 2, r)
        return min(lv, rv)


    def _query_sum(self, a, b, k, l, r):
        if(b <= l or r <= a):
            return 0

        if(a <= l and r <= b):
            return self.sum[k]

        self.push(k)
        lv = self._query_sum(a, b, 2*k+1, l, (l+r)//2)
        rv = self._query_sum(a, b, 2*k+2, (l+r)//2, r)
        return lv + rv


    # range minimize query
    def update_min(self, a, b, x):
        self._update_min(x, a, b, 0, 0, self.n0)

    # range maximize query
    def update_max(self, a, b, x):
        self._update_max(x, a, b, 0, 0, self.n0)

    # range add query
    def add_val(self, a, b, x):
        self._add_val(x, a, b, 0, 0, self.n0)

    # range update query
    def update_val(self, a, b, x):
        self._update_val(x, a, b, 0, 0, self.n0)

    # range minimum query
    def query_max(self, a, b):
        return self._query_max(a, b, 0, 0, self.n0)

    # range maximum query
    def query_min(self, a, b):
        return self._query_min(a, b, 0, 0, self.n0)

    # range sum query
    def query_sum(self, a, b):
        return self._query_sum(a, b, 0, 0, self.n0)



def main():
    S = SI()
    T = SI()
    # TとS[i:]の最長共通prefixの長さの配列
    N = len(T)
    Z = string.z_algorithm(S+"$"+T)[-N:]

    # print(Z)

    INF = 10**10
    A = [INF] * (N+1)
    A[0] = 0
    tree = SegmentTreeBeats(N+1, A)

    for i in range(N):
        z = Z[i]
        if z == 0:
            continue
        tree.update_min(i+1, i+z+1, tree.query_min(i, i+1) + 1)

        # print(i, z)
        # for j in range(N+1):
        #     print(tree.query_min(j, j+1))

    # print(tree.min_v)
    ans = tree.query_min(N, N+1)
    print(ans if ans != INF else -1)


if __name__ == "__main__":
    main()
