"""2次元KD-tree。出典: AOJ/DSL_2_C.py。空入力対応の平衡二分木。

構築O(n log²n)。点は(x,y)。検索は半開長方形。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    tree = KDTree([(0, 0), (2, 3), (1, 1)])
    sorted(tree.query(0, 0, 2, 2))  # x=2 / y=2 は含まない
    # => [0, 2]
"""


class KDTree:
    """静的な2次元点群points=[(x,y),...]を長方形で検索する。
    queryの戻り値は元の入力順の0-indexed ID。重複座標も別IDで保持する。
    構築O(n log² n)。構築後の点更新は非対応。
    入力: pointsは数値座標(x,y)の列。n=len(points)、構築O(n log²(n+1))時間・O(n)空間。
    """
    def __init__(self, points):
        """入力: pointsは数値座標(x,y)の列。n=len(points)、構築O(n log²(n+1))時間・O(n)空間。
        """
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
        """[left,right)×[bottom,top)内の点ID。結果順序は未指定。
        left/rightはxの下限/上限、bottom/topはyの下限/上限の数値。時間O(訪問ノード数)、最悪O(n)。追加空間O(log(n+1)+出力件数)。
        """
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
