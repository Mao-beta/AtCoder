"""Cartesian Tree。出典: NDPC_F.pyから問題固有DPを除去。
O(n)、0-indexed。同値なら左側を親にする最小ヒープ。空列のroot=-1。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    tree = CartesianTree([3, 1, 2])
    tree.root, tree.parent, tree.left, tree.right  # => (1, [1, -1, 1], [-1, 0, -1], [-1, 2, -1])
"""


class CartesianTree:
    """valuesを中順巡回順とする最小ヒープの二分木をO(n)で作る。
    rootは根の元配列添字。parent/left/rightは各頂点の親・左右の子の添字配列。
    存在しない親・子は-1。最小値が複数なら左側が親。空配列のroot=-1。
    入力: valuesは相互に大小比較できる値の列。N=len(values)。構築O(N)時間・空間。root/parent/left/rightは元配列の0-indexed添字。
    """
    def __init__(self, values):
        """入力: valuesは相互に大小比較できる値の列。N=len(values)。構築O(N)時間・空間。root/parent/left/rightは元配列の0-indexed添字。
        """
        n = len(values)
        self.parent, self.left, self.right = [-1] * n, [-1] * n, [-1] * n
        stack = []
        for i, value in enumerate(values):
            last = -1
            while stack and values[stack[-1]] > value:
                last = stack.pop()
            if last != -1:
                self.left[i] = last
                self.parent[last] = i
            if stack:
                self.right[stack[-1]] = i
                self.parent[i] = stack[-1]
            stack.append(i)
        self.root = stack[0] if stack else -1
