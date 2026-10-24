"""キー付き最大値取得・削除。出典: _GetMax_and_Delete.py。

同じキーの更新・削除後の再追加に対応。set/discard/top/popは償却O(log n)。
PyPy向け。値は数値、キーはhashable。キー同士の比較は不要。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    q = MaxQueue()
    q.set('a', 3); q.set('b', 7); q.set('a', 10)
    q.top(), q.pop(), q.top()  # => (('a', 10), ('a', 10), ('b', 7))
"""

from heapq import heappush, heappop, heapify


class MaxQueue:
    """キーごとに1つの数値を保持し最大値を取得する。MaxQueue()は空。
    setは同じキーを上書き、discardはキー削除。キーはhashableで大小比較不要。
    len(q)は有効キー数。遅延削除ヒープ、操作は償却O(log n)。
    引数なしで空の構造をO(1)時間・空間で作る。keyはhashableな識別子、valueは比較・符号反転できる数値。nは有効なキー数、Hは保留履歴を含むヒープの長さ。
    """
    def __init__(self):
        """引数なしで空の構造をO(1)時間・空間で作る。keyはhashableな識別子、valueは比較・符号反転できる数値。nは有効なキー数、Hは保留履歴を含むヒープの長さ。
        """
        self.heap = []
        self.current = {}
        self.serial = 0

    def __len__(self):
        return len(self.current)

    def set(self, key, value):
        """keyの値をvalueに追加・上書きする。valueは数値。戻り値なし。
        ヒープ整理・再構築を含め償却O(log(H+1))時間。単発では古い要素の掃除O(H log(H+1))や再構築O(H)があり得る。
        """
        self.serial += 1
        self.current[key] = (value, self.serial)
        heappush(self.heap, (-value, self.serial, key))
        self._compact()

    def discard(self, key):
        """keyを削除できたらTrue、未登録ならFalse。
        ヒープ整理・再構築を含め償却O(log(H+1))時間。単発では古い要素の掃除O(H log(H+1))や再構築O(H)があり得る。
        """
        if key not in self.current:
            return False
        del self.current[key]
        self._compact()
        return True

    def _compact(self):
        if len(self.heap) > max(64, 2 * len(self.current)):
            self.heap = [
                (-value, serial, key) for key, (value, serial) in self.current.items()
            ]
            heapify(self.heap)

    def top(self):
        """(キー,値)。空ならIndexError。
        ヒープ整理・再構築を含め償却O(log(H+1))時間。単発では古い要素の掃除O(H log(H+1))や再構築O(H)があり得る。
        """
        while self.heap:
            negative, serial, key = self.heap[0]
            if self.current.get(key) == (-negative, serial):
                return key, -negative
            heappop(self.heap)
        raise IndexError("empty queue")

    def pop(self):
        """最大の(キー,値)を削除して返す。同値は更新時刻が古いものから。空はIndexError。
        ヒープ整理・再構築を含め償却O(log(H+1))時間。単発では古い要素の掃除O(H log(H+1))や再構築O(H)があり得る。
        """
        key, value = self.top()
        heappop(self.heap)
        del self.current[key]
        return key, value
