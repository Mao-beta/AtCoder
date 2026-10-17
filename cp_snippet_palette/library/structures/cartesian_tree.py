"""Cartesian Tree。出典: NDPC_F.pyから問題固有DPを除去。
O(n)、0-indexed。同値なら左側を親にする最小ヒープ。空列のroot=-1。
PyPy向け。Codonでのコンパイルは未確認。
"""


class CartesianTree:
    def __init__(self, values):
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
