"""配列で持つ双方向連結リスト。出典: tessoku-book/C17.pyを汎用化。

ノードIDでO(1)挿入・削除。実ノードIDは0始まり、番兵は-1。削除IDは再利用しない。PyPy向け。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    linked = LinkedList()
    first = linked.append('a')
    second = linked.insert_after(first, 'b')
    first, second  # => (0, 1)
    linked.erase(first), list(linked)  # => ('a', ['b'])
    linked.insert_after(-1, 'head')  # => 2（先頭へ追加）
    list(linked)  # => ['head', 'b']
"""


class LinkedList:
    """空の双方向連結リスト。ノードIDによる挿入・削除はO(1)。
    実ノードIDは追加順に0,1,...。-1は先頭の直前を表す番兵。
    append/insert_afterが返すIDを保存して操作する。IDは現在の並び順の添字ではない。
    list(linked)で値を順に取得、len(linked)は生存要素数。削除IDは再利用しない。
    引数なしでO(1)時間・空間の空リストを作る。nodeはinsert_after/appendが返す整数ID、valueは任意の格納値。追加Q回に対し空間O(Q)。
    削除後のID領域も保持する。
    """
    def __init__(self):
        """引数なしでO(1)時間・空間の空リストを作る。nodeはinsert_after/appendが返す整数ID、valueは任意の格納値。追加Q回に対し空間O(Q)。
        削除後のID領域も保持する。
        """
        self.values = []
        self.prev = []
        self.next = []
        self.alive = []
        self.head = self.tail = -1
        self.size = 0

    def __len__(self):
        return self.size

    def insert_after(self, node, value):
        """生存ノードnodeの直後へvalueを追加し、新しいノードIDを返す。
        node=-1なら先頭へ追加。削除済み・存在しないIDはIndexError。
        償却O(1)時間、1要素ぶんの領域を追加する。
        """
        if node != -1 and (not 0 <= node < len(self.alive) or not self.alive[node]):
            raise IndexError(node)
        idx = len(self.values)
        successor = self.head if node == -1 else self.next[node]
        self.values.append(value)
        self.prev.append(node)
        self.next.append(successor)
        self.alive.append(True)
        if node == -1:
            self.head = idx
        else:
            self.next[node] = idx
        if successor == -1:
            self.tail = idx
        else:
            self.prev[successor] = idx
        self.size += 1
        return idx

    def append(self, value):
        """末尾にvalueを追加し、新しいノードIDを返す。
        償却O(1)時間、1要素ぶんの領域を追加する。
        """
        return self.insert_after(self.tail, value)

    def erase(self, node):
        """ノードID nodeを削除し、その値を返す。番兵・削除済みIDはIndexError。
        時間・追加空間O(1)。
        """
        if not 0 <= node < len(self.alive) or not self.alive[node]:
            raise IndexError(node)
        previous, successor = self.prev[node], self.next[node]
        if previous == -1:
            self.head = successor
        else:
            self.next[previous] = successor
        if successor == -1:
            self.tail = previous
        else:
            self.prev[successor] = previous
        self.alive[node] = False
        self.size -= 1
        return self.values[node]

    def __iter__(self):
        node = self.head
        while node != -1:
            yield self.values[node]
            node = self.next[node]
