"""ダブリング。出典: _test.py: Doubling。

終端-1、0回、表を超えるクエリに対応。前計算O(n log K)、問い合わせO(log K)。
PyPy向け。Codonではmax_stepsを64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    db = Doubling([1, 2, -1], max_steps=10)
    db.jump(0, 2), db.jump(0, 3), db.jump(1, 0)  # => (2, -1, 1)
"""


class Doubling:
    """next_vertex[v]を1回遷移先とする関数グラフ。終端は-1。
    max_stepsは後で問い合わせる最大回数（0以上）。配列を複製して前計算する。
    jump(v,k)でk回後の頂点を取得。構築O(n log K)、問い合わせO(log K)。
    入力: next_vertexは長さNの整数列。next_vertex[v]は0..N-1の遷移先、-1は終端。max_stepsは問い合わせる最大非負回数K。
    構築はO(N*(1+log(K+1)))時間・空間。
    """
    def __init__(self, next_vertex, max_steps):
        """入力: next_vertexは長さNの整数列。next_vertex[v]は0..N-1の遷移先、-1は終端。max_stepsは問い合わせる最大非負回数K。
        構築はO(N*(1+log(K+1)))時間・空間。
        """
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
        """vertexからsteps回後の頂点番号。終端に到達したら-1。
        steps=0ならvertexを返す。0<=steps<=max_stepsが必要で、上限超過はValueError。
        vertexは-1または0..N-1の頂点番号、stepsは非負整数。時間O(1+log(steps+1))、追加空間O(1)。
        """
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
