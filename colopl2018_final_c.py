import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


from collections import deque

class ConvexHullTrick():
    """
    追加する直線の傾きが単調減少、計算する x 座標が単調増加するときに、
    直線(y = ai*x + bi)の追加とmin_i f(x)を計算 O(N+Q)
    """
    def __init__(self):
        self.deq = deque()

    def check(self, f1, f2, f3):
        return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])

    def f(self, f1, x):
        return f1[0] * x + f1[1]

    # add f_i(x)=a*x+b
    def add_line(self, a, b):
        f1 = (a, b)
        while len(self.deq) >= 2 and self.check(self.deq[-2], self.deq[-1], f1):
            self.deq.pop()
        self.deq.append(f1)

    # min f_i(x)
    def query(self, x):
        while len(self.deq) >= 2 and self.f(self.deq[0], x) >= self.f(self.deq[1], x):
            self.deq.popleft()
        return self.f(self.deq[0], x)


class LiChaoInt:
    """
    非再帰・動的 Li Chao 木（整数クエリ専用）。

    直線 y = m*x + b を順不同で追加し、任意の整数 x に対する最小値/最大値を高速に求める。

    特徴
    ----
    - x 座標は「整数」を想定（区間 [xmin, xmax] を両端含む）
    - 直線の追加順・クエリ順に単調性は不要
    - 非再帰（while ループのみ）で PyPy でも動かしやすい
    - ノードはオブジェクトではなく配列で管理（生成コストを抑える）
    - mode="min"/"max" で最小/最大を切替可能
    - デフォルト区間は [-10**18, 10**18]

    計算量
    ------
    - add_line / query ともに最悪 O(log2(xmax-xmin+1))
      例: [-10**18, 10**18] なら深さはおよそ 61

    注意
    ----
    - query(x) の x は必ず xmin <= x <= xmax を満たす必要があります。
      はみ出す可能性がある場合は、xmin/xmax を十分広く取ってください。
    """

    __slots__ = ("xmin", "xmax", "is_min", "m", "b", "lc", "rc", "root", "INF")

    def __init__(self, xmin: int = -10**18, xmax: int = 10**18, mode: str = "min"):
        assert xmin <= xmax
        assert mode in ("min", "max")
        self.xmin = xmin
        self.xmax = xmax
        self.is_min = (mode == "min")

        # ノード配列（index がノードID）
        self.m = []    # 傾き
        self.b = []    # 切片
        self.lc = []   # 左子（なければ -1）
        self.rc = []   # 右子（なければ -1）
        self.root = -1

        # 十分大きい番兵
        self.INF = 10**60

    def _new_node(self, m: int, b: int) -> int:
        idx = len(self.m)
        self.m.append(m)
        self.b.append(b)
        self.lc.append(-1)
        self.rc.append(-1)
        return idx

    def _better(self, y_new: int, y_cur: int) -> bool:
        """y_new が y_cur より良い（minなら小さい / maxなら大きい）なら True"""
        return y_new < y_cur if self.is_min else y_new > y_cur

    def _combine(self, best: int, cand: int) -> int:
        """best と cand のうち良い方を返す"""
        return cand if self._better(cand, best) else best

    @staticmethod
    def _eval(m: int, b: int, x: int) -> int:
        return m * x + b

    def add_line(self, m_new: int, b_new: int) -> None:
        """
        直線 y = m_new*x + b_new を追加します（区間全体で有効）。

        Parameters
        ----------
        m_new : int
            傾き
        b_new : int
            切片
        """
        if self.root == -1:
            self.root = self._new_node(m_new, b_new)
            return

        node = self.root
        l = self.xmin
        r = self.xmax

        while True:
            mid = (l + r) >> 1

            # 現在ノードに保持している直線
            m_cur = self.m[node]
            b_cur = self.b[node]

            # mid で比較して、mid で良い方を node に残す
            y_cur_mid = m_cur * mid + b_cur
            y_new_mid = m_new * mid + b_new
            if self._better(y_new_mid, y_cur_mid):
                # node と new を swap
                self.m[node], m_new = m_new, m_cur
                self.b[node], b_new = b_new, b_cur
                m_cur = self.m[node]
                b_cur = self.b[node]

            if l == r:
                return

            # node は mid で勝っている。new が勝てる可能性がある側だけに降ろす。
            y_cur_l = m_cur * l + b_cur
            y_new_l = m_new * l + b_new
            y_cur_r = m_cur * r + b_cur
            y_new_r = m_new * r + b_new

            if self._better(y_new_l, y_cur_l):
                # 左側で new が勝てる -> 左へ
                nxt = self.lc[node]
                if nxt == -1:
                    self.lc[node] = self._new_node(m_new, b_new)
                    return
                node = nxt
                r = mid
            elif self._better(y_new_r, y_cur_r):
                # 右側で new が勝てる -> 右へ
                nxt = self.rc[node]
                if nxt == -1:
                    self.rc[node] = self._new_node(m_new, b_new)
                    return
                node = nxt
                l = mid + 1
            else:
                # 区間全体で new が勝てない
                return

    def query(self, x: int) -> int:
        """
        追加済み直線の中で、x における最小値/最大値を返します。

        Parameters
        ----------
        x : int
            クエリ座標（整数）。xmin <= x <= xmax を満たす必要があります。

        Returns
        -------
        int
            mode="min" のとき最小値、mode="max" のとき最大値。
            まだ直線が1本も追加されていない場合は、minなら +INF、maxなら -INF を返します。
        """
        assert self.xmin <= x <= self.xmax

        if self.root == -1:
            return self.INF if self.is_min else -self.INF

        node = self.root
        l = self.xmin
        r = self.xmax
        best = self.INF if self.is_min else -self.INF

        while node != -1:
            best = self._combine(best, self.m[node] * x + self.b[node])
            if l == r:
                break
            mid = (l + r) >> 1
            if x <= mid:
                node = self.lc[node]
                r = mid
            else:
                node = self.rc[node]
                l = mid + 1

        return best


def main():
    N = NI()
    A = NLI()
    CHT = LiChaoInt(0, 10**18, mode="min")
    for j, a in enumerate(A, start=1):
        CHT.add_line(-2*j, a+j**2)
    for i in range(N):
        print(CHT.query(i+1) + (i+1)**2)


if __name__ == "__main__":
    main()
