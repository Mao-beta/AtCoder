"""ダブリング。出典: _test.py: Doubling。
終端-1、0回、表を超えるクエリに対応。前計算O(n log K)、問い合わせO(log K)。
PyPy向け。Codonではmax_stepsを64bit以内にする。
"""


class Doubling:
    def __init__(self, next_vertex, max_steps):
        if max_steps < 0:
            raise ValueError("max_steps must be nonnegative")
        self.n = len(next_vertex)
        if any(v < -1 or v >= self.n for v in next_vertex):
            raise ValueError("invalid successor")
        self.max_steps = max_steps
        self.table = [list(next_vertex)]
        for _ in range(1, max(1, max_steps.bit_length())):
            row = self.table[-1]
            self.table.append([-1 if v == -1 else row[v] for v in row])

    def jump(self, vertex, steps):
        if not 0 <= steps <= self.max_steps:
            raise ValueError("steps exceeds the built table")
        if not -1 <= vertex < self.n:
            raise IndexError(vertex)
        bit = 0
        while steps and vertex != -1:
            if steps & 1:
                vertex = self.table[bit][vertex]
            steps >>= 1
            bit += 1
        return vertex
