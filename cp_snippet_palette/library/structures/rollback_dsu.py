"""Rollback Union-Find。経路圧縮をせず、併合を過去の時点へ巻き戻す。
構築O(n)、merge/leader/same/sizeはO(log n)、undoはO(1)。
永続Union-Findのクエリを版の木にしてDFSする場合などに使う。オンライン永続ではない。
PyPy向け。Codonでは未確認。頂点は0-indexed。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    d = RollbackDSU(4)
    mark = d.snapshot()
    d.merge(0, 1)
    d.same(0, 1), d.size(0)  # => (True, 2)
    d.rollback(mark)
    d.same(0, 1), d.components  # => (False, 4)
"""


class RollbackDSU:
    """n個の単集合から始める。mergeはACLと同じく併合後の代表を返す。
    同じ集合のmergeもundoの1回に数える。componentsは現在の連結成分数。
    snapshotは現在の履歴長であり、巻き戻した先の履歴を再利用することはできない。
    入力: nは頂点数の非負整数N。構築O(N)時間・空間。a/bは0..N-1の頂点番号。merge Q回ぶんの履歴で全体O(N+Q)空間。
    """

    def __init__(self, n):
        """入力: nは頂点数の非負整数N。構築O(N)時間・空間。a/bは0..N-1の頂点番号。merge Q回ぶんの履歴で全体O(N+Q)空間。
        """
        self._parent = [-1] * n
        self._history = []
        self.components = n

    def leader(self, a):
        """aの代表頂点を返す。O(log n)。"""
        while self._parent[a] >= 0:
            a = self._parent[a]
        return a

    def merge(self, a, b):
        """a,bの集合を併合し代表を返す。O(log n)、履歴を1件積む。"""
        a, b = self.leader(a), self.leader(b)
        if a == b:
            self._history.append(None)
            return a
        p = self._parent
        if p[a] > p[b]:
            a, b = b, a
        self._history.append((a, p[a], b, p[b]))
        p[a] += p[b]
        p[b] = a
        self.components -= 1
        return a

    def same(self, a, b):
        """a,bが同じ集合かをboolで返す。O(log n)。"""
        return self.leader(a) == self.leader(b)

    def size(self, a):
        """aを含む集合の要素数。O(log n)。"""
        return -self._parent[self.leader(a)]

    def snapshot(self):
        """現在の履歴長を返す。rollbackへ渡す保存点。O(1)。"""
        return len(self._history)

    def undo(self):
        """最後のmergeを1回取り消す。履歴が空ならIndexError。O(1)。"""
        item = self._history.pop()
        if item is not None:
            a, pa, b, pb = item
            self._parent[a], self._parent[b] = pa, pb
            self.components += 1

    def rollback(self, mark):
        """snapshotで保存した履歴長markへ戻す。取り消すmerge数に比例。
        markはsnapshot()で得た整数の履歴長。取り消す操作数Dに対し時間O(D)、追加空間O(1)。
        """
        if not 0 <= mark <= len(self._history):
            raise ValueError("snapshot is outside the current history")
        while len(self._history) > mark:
            self.undo()
