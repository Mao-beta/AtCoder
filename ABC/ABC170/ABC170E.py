import sys
import math
from collections import defaultdict
from heapq import heappop, heappush

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class KinderGarden:
    def __init__(self):
        self.neg = []
        self.out = []
        self.dic = defaultdict(lambda: None)

    def exist(self, key):
        if self.dic[key] is None:
            return False
        else:
            return True

    def add(self, val, key):
        if self.exist(key):
            return

        heappush(self.neg, (-val, key))
        self.dic[key] = val

    def _del(self, key):
        del self.dic[key]

    def delete(self, key):
        val = self.dic[key]
        if val is None:
            raise ValueError("You will delete not-exist key")
        heappush(self.out, (-val, key))
        self._del(key)

    def get_max(self):
        while self.neg and self.out:
            if self.neg[0][1] == self.out[0][1]:
                heappop(self.neg)
                heappop(self.out)
            else:
                break

        if not self.neg:
            return None, None

        val, key = self.neg[0][0] * (-1), self.neg[0][1]
        return val, key


# SegTreeの関数
def segfunc(x, y):
    return min(x, y)


# 単位元
# min->inf, max->-inf, add->0, mul->1
INF = 1<<60
ide_ele = INF


# セグメント木
class SegTree:
    """
    init(init_val, segfunc, ide_ele): 配列init_valで初期化、構築
    update(k, x): k番目の値をxに更新
    query(l, r): 区間[l, r)をsegfuncしたものを返す
    """

    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセットする
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        :param k: index(0-index)
        :param x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        :param l: 0-index
        :param r: 0-index
        :return:
        """
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

    def __repr__(self):
        return str(self.tree[self.num:])


def main():
    N, Q = NMI()
    max_kg = 200000
    KG = [KinderGarden() for _ in range(max_kg)]
    now = [-1] * N
    Val = [0] * N

    for key in range(N):
        val, kg = NMI()
        kg -= 1
        KG[kg].add(val, key)
        now[key] = kg
        Val[key] = val

    seg = SegTree(init_val=[INF]*max_kg, segfunc=segfunc, ide_ele=ide_ele)
    for i, K in enumerate(KG):
        M = K.get_max()[0]
        if M:
            seg.update(i, M)
        else:
            pass

    #print(seg)
    for i in range(Q):
        key, kg_to = NMI()
        key -= 1
        kg_to -= 1
        kg_from = now[key]
        K_from = KG[kg_from]
        K_to = KG[kg_to]

        #print(key, kg_from, kg_to)
        #print(K_from.dic.items())
        K_from.delete(key)
        K_to.add(Val[key], key)

        from_next_max = K_from.get_max()[0] or INF
        to_next_max = K_to.get_max()[0] or INF
        #print(from_next_max, to_next_max)

        seg.update(kg_from, from_next_max)
        seg.update(kg_to, to_next_max)
        now[key] = kg_to

        #print(seg)
        print(seg.query(0, max_kg))


if __name__ == "__main__":
    main()