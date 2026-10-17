"""直線・区間限定直線の最小/最大。LiChaoTreeは座標圧縮版。
LiChaoIntは整数定義域[xmin,xmax]の旧API。LiChaoTree.add_segmentは半開区間。
抽出元: colopl2018_final_c.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。
"""

from bisect import bisect_left


class LiChaoTree:
    """問い合わせ座標xsを先に登録するLi Chao木。重複・順不同可。
    add_lineはO(log n)、add_segmentはO(log^2 n)、queryはO(log n)。
    空間O(n+追加本数)。mode='min'/'max'。入力xsを変更しない。
    """

    def __init__(self, xs, mode="min"):
        if mode not in ("min", "max"):
            raise ValueError("mode must be min or max")
        self.xs = sorted(set(xs))
        self.n = len(self.xs)
        self.size = 1 << (max(1, self.n) - 1).bit_length()
        self._xs = self.xs + [self.xs[-1] if self.n else 0] * (self.size - self.n)
        self._tree = [-1] * (2 * self.size)
        self._lines = []
        self._sign = 1 if mode == "min" else -1

    def _insert(self, line, node, left, right):
        xs, tree, lines = self._xs, self._tree, self._lines
        while True:
            old = tree[node]
            if old == -1:
                tree[node] = line
                return
            middle = (left + right) // 2
            a, b = lines[line]
            c, d = lines[old]
            if a * xs[middle] + b < c * xs[middle] + d:
                tree[node], line = line, old
                a, b, c, d = c, d, a, b
            if right - left == 1:
                return
            if a * xs[left] + b < c * xs[left] + d:
                node, right = node * 2, middle
            elif a * xs[right - 1] + b < c * xs[right - 1] + d:
                node, left = node * 2 + 1, middle
            else:
                return

    def add_line(self, a, b):
        """全登録座標で有効なy=a*x+bを追加。"""
        if self.n:
            self._lines.append((a * self._sign, b * self._sign))
            self._insert(len(self._lines) - 1, 1, 0, self.size)

    def add_segment(self, left, right, a, b):
        """座標の半開区間[left,right)だけにy=a*x+bを追加。空区間は何もしない。"""
        if left > right:
            raise ValueError("left must not exceed right")
        start, stop = bisect_left(self.xs, left), bisect_left(self.xs, right)
        if start == stop:
            return
        line = len(self._lines)
        self._lines.append((a * self._sign, b * self._sign))
        stack = [(1, 0, self.size)]
        while stack:
            node, lo, hi = stack.pop()
            if stop <= lo or hi <= start:
                continue
            if start <= lo and hi <= stop:
                self._insert(line, node, lo, hi)
                continue
            middle = (lo + hi) // 2
            stack.append((node * 2, lo, middle))
            stack.append((node * 2 + 1, middle, hi))

    def query(self, x):
        """xでの最小/最大値。有効な直線なしならNone。未登録座標はValueError。"""
        index = bisect_left(self.xs, x)
        if index == self.n or self.xs[index] != x:
            raise ValueError("query coordinate was not registered")
        node = index + self.size
        best = None
        while node:
            line = self._tree[node]
            if line != -1:
                a, b = self._lines[line]
                value = a * x + b
                if best is None or value < best:
                    best = value
            node >>= 1
        return None if best is None else best * self._sign


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

    __slots__ = ("xmin", "xmax", "is_min", "m", "b", "lc", "rc", "root")

    def __init__(self, xmin: int = -(10**18), xmax: int = 10**18, mode: str = "min"):
        assert xmin <= xmax
        assert mode in ("min", "max")
        self.xmin = xmin
        self.xmax = xmax
        self.is_min = mode == "min"

        # ノード配列（index がノードID）
        self.m = []  # 傾き
        self.b = []  # 切片
        self.lc = []  # 左子（なければ -1）
        self.rc = []  # 右子（なければ -1）
        self.root = -1

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
            直線が1本もない場合はIndexError。
        """
        assert self.xmin <= x <= self.xmax

        if self.root == -1:
            raise IndexError("no lines")

        node = self.root
        l = self.xmin
        r = self.xmax
        best = self.m[node] * x + self.b[node]

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
