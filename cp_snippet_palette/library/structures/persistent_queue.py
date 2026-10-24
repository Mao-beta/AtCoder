"""二分累乗による完全永続キュー。任意の過去版から分岐できる。
操作数Qに対して追加は償却O(log Q)、削除はO(log Q)、全体の空間O(Q log Q)。
祖先表は32bit配列で保持する。2^31ノード未満。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    q = PersistentQueue()  # 版0は空
    v1 = q.append(0, 10)
    v2 = q.append(v1, 20)
    v3, x = q.popleft(v2)
    x, q.front(v3), q.front(v2), q.size(v2)  # => (10, 20, 10, 2)
    v4 = q.append(v1, 99)  # v1から別の版へ分岐
    q.size(v4)  # => 2
"""

from array import array


class PersistentQueue:
    """版番号で操作するキュー。append/popleftは新しい版を作り、元の版を保持する。
    版0は空。size/frontは版を作らない。値そのものはコピーしないので変更しないこと。
    引数なしで空の版0をO(1)時間・空間で作る。versionは過去に返した版番号（整数）、valueは任意の格納値。Qは累計操作数、全体空間O(Q log(Q+1))。
    """

    def __init__(self):
        """引数なしで空の版0をO(1)時間・空間で作る。versionは過去に返した版番号（整数）、valueは任意の格納値。Qは累計操作数、全体空間O(Q log(Q+1))。
        """
        self._values = [None]
        self._up = [array("i", [0])]
        self._back = [0]
        self._size = [0]

    def size(self, version):
        """指定版の要素数。O(1)。"""
        return self._size[version]

    def append(self, version, value):
        """指定版の末尾へvalueを追加した新しい版番号を返す。
        時間は償却O(log(Q+1))。祖先表の段数を増やす1回はO(Q)になることがある。versionは既存の版番号。
        """
        node = len(self._values)
        self._values.append(value)
        up = self._up
        if node >= 1 << len(up):
            up.append(array("i", [0]) * node)
        up[0].append(self._back[version])
        for k in range(1, len(up)):
            up[k].append(up[k - 1][up[k - 1][node]])
        self._back.append(node)
        self._size.append(self._size[version] + 1)
        return len(self._back) - 1

    def front(self, version):
        """指定版の先頭値。空ならIndexError。O(log Q)。"""
        steps = self._size[version] - 1
        if steps < 0:
            raise IndexError("front of empty queue")
        node, bit = self._back[version], 0
        while steps:
            if steps & 1:
                node = self._up[bit][node]
            steps >>= 1
            bit += 1
        return self._values[node]

    def popleft(self, version):
        """先頭を除いた(新しい版番号, 削除した値)を返す。空ならIndexError。O(log Q)。"""
        value = self.front(version)
        self._back.append(self._back[version])
        self._size.append(self._size[version] - 1)
        return len(self._back) - 1, value
