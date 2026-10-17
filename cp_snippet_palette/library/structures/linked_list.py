"""配列で持つ双方向連結リスト。出典: tessoku-book/C17.pyを汎用化。
ノードIDでO(1)挿入・削除。ID=0は番兵。削除IDは再利用しない。PyPy向け。
"""


class LinkedList:
    def __init__(self):
        self.values = [None]
        self.prev = [0]
        self.next = [0]
        self.alive = [True]
        self.size = 0

    def __len__(self):
        return self.size

    def insert_after(self, node, value):
        if not 0 <= node < len(self.alive) or not self.alive[node]:
            raise IndexError(node)
        idx = len(self.values)
        successor = self.next[node]
        self.values.append(value)
        self.prev.append(node)
        self.next.append(successor)
        self.alive.append(True)
        self.next[node] = self.prev[successor] = idx
        self.size += 1
        return idx

    def append(self, value):
        return self.insert_after(self.prev[0], value)

    def erase(self, node):
        if not 0 < node < len(self.alive) or not self.alive[node]:
            raise IndexError(node)
        self.next[self.prev[node]] = self.next[node]
        self.prev[self.next[node]] = self.prev[node]
        self.alive[node] = False
        self.size -= 1
        return self.values[node]

    def __iter__(self):
        node = self.next[0]
        while node:
            yield self.values[node]
            node = self.next[node]
