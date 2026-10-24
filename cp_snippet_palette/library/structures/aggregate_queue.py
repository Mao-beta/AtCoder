"""SWAG: 結合的な演算のキュー集約。非可換な関数合成にも対応。
append/popleftは償却O(1)回のop、prodはO(1)回のop、空間O(n)。
op(x,y)は左側xの後ろにyを連結した集約。opは引数を変更しないこと。
PyPy向け。Codonでは要素・単位元・opの戻り値を同じ型にする。コンパイル未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    q = AggregateQueue(lambda a, b: a + b, 0)
    q.append(3); q.append(5)
    q.prod(), q.popleft(), q.prod()  # => (8, 3, 5)

一次関数f(x)=a*x+bを順に適用するなら、op(f,g)=g∘fとする。
    mod = 998244353
    compose = lambda f, g: (g[0]*f[0] % mod, (g[0]*f[1]+g[1]) % mod)
    q = AggregateQueue(compose, (1, 0))
    q.append((2, 1)); q.append((3, 4))
    a, b = q.prod()
    (a * 10 + b) % mod  # => 67
"""


class AggregateQueue:
    """結合的演算opと左右の単位元eを指定する集約キュー。
    prod()は先頭から末尾の順に集約する。opは引数を変更しないこと。
    append/popleftは償却O(1)回、prodはO(1)回のop。len(q)は要素数。
    入力: opは二つの集約値を同じ型の値へ結合する関数、eは左右の単位元。opは結合則を満たし引数を変更しないこと。構築O(1)時間・空間。valueはopが受け取れる要素。
    Nは現在の要素数、保持領域O(N)。以下はopと要素のコピーをO(1)とした計算量。
    """

    def __init__(self, op, e):
        """入力: opは二つの集約値を同じ型の値へ結合する関数、eは左右の単位元。opは結合則を満たし引数を変更しないこと。構築O(1)時間・空間。valueはopが受け取れる要素。
        Nは現在の要素数、保持領域O(N)。以下はopと要素のコピーをO(1)とした計算量。
        """
        self.op = op
        self.e = e
        self._front = []
        self._back = []

    def __len__(self):
        return len(self._front) + len(self._back)

    def append(self, value):
        """末尾へ追加する。
        時間は償却O(1)回のop、1回の再配置は最悪O(N)。
        """
        back = self._back
        total = self.op(back[-1][1], value) if back else value
        back.append((value, total))

    def popleft(self):
        """先頭を削除して返す。空ならIndexError。
        時間は償却O(1)回のop、1回の再配置は最悪O(N)。
        """
        if not self._front:
            while self._back:
                value = self._back.pop()[0]
                total = self.op(value, self._front[-1][1]) if self._front else value
                self._front.append((value, total))
        if not self._front:
            raise IndexError("pop from empty queue")
        return self._front.pop()[0]

    def prod(self):
        """キュー全体の集約。空なら単位元。
        時間・追加空間O(1)回のop。
        """
        if not self._front:
            return self._back[-1][1] if self._back else self.e
        if not self._back:
            return self._front[-1][1]
        return self.op(self._front[-1][1], self._back[-1][1])

    def clear(self):
        """全要素を削除し、prod()が単位元eを返す状態に戻す。戻り値なし。
        時間O(N)（保持参照の解放）、追加空間O(1)。
        """
        self._front.clear()
        self._back.clear()
