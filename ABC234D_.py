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


class BalancingPivotTree:
    """
    元とさせていただいたアイデア・コード
    https://qiita.com/Kiri8128/items/6256f8559f0026485d90
    ・個数を管理し、多重集合を管理できるようにした
    ・K番目を取得できるようにした

    Features:
    append(v)
    delete(v)
    get_kth(k)
    find_l(v)
    find_r(v)
    min
    max
    """

    def __init__(self, n):
        self.N = n
        self.root = self.node(1 << n, 1 << n)
        self.count = {1 << n: 1}

    def append(self, v):
        """ v (0 <= v <= 2^n-2) を追加 """
        v += 1

        if v in self.count:
            self.count[v] += 1
        else:
            self.count[v] = 1
        inc = 1

        nd = self.root
        while True:
            nd.subtree_count += inc
            if v == nd.value:
                # v がすでに存在する場合に何か処理が必要ならここに書く
                return 0
            else:
                mi, ma = min(v, nd.value), max(v, nd.value)
                if mi < nd.pivot:
                    if nd.value != ma:
                        inc = self.count[mi]
                    nd.value = ma
                    if nd.left:
                        nd = nd.left
                        v = mi
                    else:
                        p = nd.pivot
                        nd.left = self.node(mi, p - (p & -p) // 2)
                        nd.left.subtree_count = self.count[mi]
                        break
                else:
                    if nd.value != mi:
                        inc = self.count[ma]
                    nd.value = mi
                    if nd.right:
                        nd = nd.right
                        v = ma
                    else:
                        p = nd.pivot
                        nd.right = self.node(ma, p + (p & -p) // 2)
                        nd.right.subtree_count = self.count[ma]
                        break

    def leftmost(self, nd):
        if nd.left: return self.leftmost(nd.left)
        return nd

    def rightmost(self, nd):
        if nd.right: return self.rightmost(nd.right)
        return nd

    def find_l(self, v):
        """ vより真に小さいやつの中での最大値（なければ-1） """
        v += 1
        nd = self.root
        prev = 0
        if nd.value < v: prev = nd.value
        while True:
            if v <= nd.value:
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                prev = nd.value
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    def find_r(self, v):
        """ vより真に大きいやつの中での最小値（なければRoot） """
        v += 1
        nd = self.root
        prev = 0
        if nd.value > v: prev = nd.value
        while True:
            if v < nd.value:
                prev = nd.value
                if nd.left:
                    nd = nd.left
                else:
                    return prev - 1
            else:
                if nd.right:
                    nd = nd.right
                else:
                    return prev - 1

    @property
    def max(self):
        return self.find_l((1 << self.N) - 1)

    @property
    def min(self):
        return self.find_r(-1)

    def delete(self, v, nd=None, prev=None, dec=1):
        """ 値がvの要素を1個削除（なければ何もしない） """
        v += 1

        needs_delete = True
        if nd is None:
            if v not in self.count:
                return
            elif self.count[v] == 1:
                del self.count[v]
            else:
                self.count[v] -= 1
                needs_delete = False
            nd = self.root

        if prev is None:
            prev = nd

        while v != nd.value:
            prev = nd
            if v <= nd.value:
                if nd.left:
                    nd.subtree_count -= dec
                    nd = nd.left
                else:
                    #####
                    return
            else:
                if nd.right:
                    nd.subtree_count -= dec
                    nd = nd.right
                else:
                    #####
                    return

        nd.subtree_count -= dec
        if not needs_delete:
            return

        if (not nd.left) and (not nd.right):
            if not prev.left:
                prev.right = None
            elif not prev.right:
                prev.left = None
            else:
                if nd.pivot == prev.left.pivot:
                    prev.left = None
                else:
                    prev.right = None

        elif nd.right:
            # print("type A", v)
            nd.value = self.leftmost(nd.right).value
            self.delete(nd.value - 1, nd.right, nd, self.count[nd.value])
        else:
            # print("type B", v)
            nd.value = self.rightmost(nd.left).value
            self.delete(nd.value - 1, nd.left, nd, self.count[nd.value])

    def get_kth(self, k: int):
        """
        k番目を取得。現存する要素数より大きい数を指定すると-1
        :param k:
        :return:
        """
        nd = self.root
        if nd.subtree_count - 1 < k:
            return -1

        while True:
            cnt = self.count[nd.value]
            if nd.left is None:
                if k <= cnt:
                    return nd.value - 1
                assert nd.right is not None
                k -= cnt
                nd = nd.right

            else:
                if nd.left.subtree_count >= k:
                    nd = nd.left
                elif nd.left.subtree_count + cnt >= k:
                    return nd.value - 1
                else:
                    assert nd.right is not None
                    k -= nd.left.subtree_count + cnt
                    nd = nd.right

    def __contains__(self, v: int) -> bool:
        return v + 1 in self.count

    class node:
        def __init__(self, v, p):
            self.value = v
            self.pivot = p
            self.left = None
            self.right = None
            self.subtree_count = 1

        def __repr__(self):
            lch = self.left.value - 1 if self.left else -1
            rch = self.right.value - 1 if self.right else -1
            return f'({self.value - 1}, {self.pivot}, {lch}, {rch}, {self.subtree_count})'

    def debug(self):

        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value: re.append(str(nd))
            if nd.right:
                re += debug_node(nd.right)
            return re

        print("Debug - root =", self.root.value - 1, debug_node(self.root)[:50])
        print('Debug ', self.count)

    def debug_list(self):
        def debug_node(nd):
            re = []
            if nd.left:
                re += debug_node(nd.left)
            if nd.value:
                re.extend([nd.value - 1] * self.count[nd.value])
            if nd.right:
                re += debug_node(nd.right)
            return re

        return debug_node(self.root)[:-1]

    def debug_count(self, nd=None):
        if nd is None:
            nd = self.root
        lch = nd.left.subtree_count if nd.left is not None else 0
        rch = nd.right.subtree_count if nd.right is not None else 0
        if nd.subtree_count != lch + rch + self.count[nd.value]:
            print('NG!!', nd, lch, rch, self.count[nd.value])
            print(self.debug_list())
            print(self.count)
        if lch != 0:
            self.debug_count(nd.left)
        if rch != 0:
            self.debug_count(nd.right)


def main():
    N, K = NMI()
    P = NLI()
    BT = BalancingPivotTree(20)

    for i, p in enumerate(P, start=1):
        if i <= K-1:
            BT.append(p)
        else:
            BT.append(p)
            print(BT.get_kth(i-K+1))


if __name__ == "__main__":
    main()
