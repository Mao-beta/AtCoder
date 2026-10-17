"""2次元KD-tree。出典: AOJ/DSL_2_C.py。空入力対応の平衡二分木。
構築O(n log²n)。点は(x,y)。検索は半開長方形。PyPy向け、Codon未確認。
"""


class KDTree:
    def __init__(self, points):
        self.points = list(points)
        self.nodes = []

        def build(ids, depth):
            if not ids:
                return -1
            axis = depth & 1
            ids.sort(key=lambda i: self.points[i][axis])
            mid = len(ids) // 2
            v = ids[mid]
            left = build(ids[:mid], depth + 1)
            right = build(ids[mid + 1 :], depth + 1)
            x, y = self.points[v]
            xmin = xmax = x
            ymin = ymax = y
            for child in (left, right):
                if child != -1:
                    _, _, _, a, b, c, d = self.nodes[child]
                    xmin, xmax = min(xmin, a), max(xmax, b)
                    ymin, ymax = min(ymin, c), max(ymax, d)
            index = len(self.nodes)
            self.nodes.append((v, left, right, xmin, xmax, ymin, ymax))
            return index

        self.root = build(list(range(len(self.points))), 0)

    def query(self, left, bottom, right, top):
        """[left,right)×[bottom,top)内の点ID。結果順序は未指定。"""
        if left > right or bottom > top:
            raise ValueError("reversed rectangle")
        result = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node == -1:
                continue
            v, lc, rc, xmin, xmax, ymin, ymax = self.nodes[node]
            if right <= xmin or xmax < left or top <= ymin or ymax < bottom:
                continue
            x, y = self.points[v]
            if left <= x < right and bottom <= y < top:
                result.append(v)
            stack.extend((lc, rc))
        return result
