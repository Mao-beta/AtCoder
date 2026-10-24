"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    d = Deque([1, 2, 3])
    d.appendleft(0); d.append(4); d[1] = 10
    d[0], d[-1], list(d)  # => (0, 4, [0, 10, 2, 3, 4])
    d.popleft(), d.pop()  # => (0, 4)
    d.rotate(1)
    list(d)  # => [3, 10, 2]
"""

class Deque:
    """リングバッファによる両端キュー。整数添字でのランダムアクセス O(1)。

    Deque(src_arr=None, max_size=8)。max_size は初期予約容量（上限ではない）。
    append/appendleft/pop/popleft は償却 O(1)、添字取得・代入 O(1)。
    extend と走査は O(k)、rotate は O(min(k mod N, N-k mod N))。
    必要時に容量を倍増させる。大容量の事前確保が必要なら max_size を指定。
    入力: src_arrは初期要素のiterableまたはNone、max_sizeは初期予約容量の整数。Nは初期要素数、C=max(N,max_size)程度の予約容量。
    構築O(C+1)時間・空間。xは任意の要素、kは符号付き整数の回転量。
    """

    def __init__(self, src_arr=None, max_size=8):
        """入力: src_arrは初期要素のiterableまたはNone、max_sizeは初期予約容量の整数。Nは初期要素数、C=max(N,max_size)程度の予約容量。
        構築O(C+1)時間・空間。xは任意の要素、kは符号付き整数の回転量。
        """
        arr = [] if src_arr is None else list(src_arr)
        self.N = max(1, max_size, len(arr))
        self.buf = arr + [None] * (self.N - len(arr))
        self.head = 0
        self._size = len(arr)
        self.tail = self._size % self.N

    def __len__(self):
        return self._size

    def is_full(self):
        """現在の予約容量が埋まっているかを返す。Trueでも追加時に自動拡張する。
        時間・追加空間O(1)。
        """
        return self._size == self.N

    def is_empty(self):
        """要素数が0ならTrue。len(d)==0と同じ。
        時間・追加空間O(1)。
        """
        return self._size == 0

    def __index(self, i):
        n = self._size
        if not -n <= i < n:
            raise IndexError("deque index out of range")
        if i < 0:
            i += n
        return (self.head + i) % self.N

    def __grow(self):
        old, capacity = self.buf, self.N
        self.N *= 2
        self.buf = [old[(self.head + i) % capacity] for i in range(self._size)]
        self.buf.extend([None] * (self.N - self._size))
        self.head = 0
        self.tail = self._size

    def append(self, x):
        """右端へxを1個追加する。戻り値なし。
        償却O(1)時間。容量拡大する1回はO(N)時間・領域を使う。
        """
        if self.is_full():
            self.__grow()
        self.buf[self.tail] = x
        self.tail = (self.tail + 1) % self.N
        self._size += 1

    def appendleft(self, x):
        """左端へxを1個追加する。戻り値なし。
        償却O(1)時間。容量拡大する1回はO(N)時間・領域を使う。
        """
        if self.is_full():
            self.__grow()
        self.head = (self.head - 1) % self.N
        self.buf[self.head] = x
        self._size += 1

    def pop(self):
        """右端を削除して値を返す。空ならIndexError。
        時間・追加空間O(1)。
        """
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        self.tail = (self.tail - 1) % self.N
        x = self.buf[self.tail]
        self.buf[self.tail] = None
        self._size -= 1
        return x

    def popleft(self):
        """左端を削除して値を返す。空ならIndexError。
        時間・追加空間O(1)。
        """
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        x = self.buf[self.head]
        self.buf[self.head] = None
        self.head = (self.head + 1) % self.N
        self._size -= 1
        return x

    def extend(self, iterable):
        """iterableを順に右端へ追加する。戻り値なし。O(k)。
        """
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable):
        """iterableを順に左端へ追加するため、入力の並びが逆になる。O(k)。
        """
        for x in iterable:
            self.appendleft(x)

    def rotate(self, k=1):
        """右に k 個回転。負数は左回転。
        現在の要素数Nに対しt=k mod Nとして時間O(1+min(t,N-t))、追加空間O(1)。空の場合O(1)。
        """
        if not self._size:
            return
        k %= self._size
        if k <= self._size - k:
            for _ in range(k):
                self.appendleft(self.pop())
        else:
            for _ in range(self._size - k):
                self.append(self.popleft())

    def clear(self):
        """全要素を削除する。予約容量は保持する。戻り値なし。
        予約容量Cに対しO(C)時間・空間（新しいバッファを確保）。
        """
        self.buf = [None] * self.N
        self.head = self.tail = self._size = 0

    def __getitem__(self, i):
        return self.buf[self.__index(i)]

    def __setitem__(self, i, x):
        self.buf[self.__index(i)] = x

    def __iter__(self):
        for i in range(self._size):
            yield self.buf[(self.head + i) % self.N]

    def __reversed__(self):
        for i in range(self._size - 1, -1, -1):
            yield self.buf[(self.head + i) % self.N]

    def __repr__(self):
        return f"Deque({list(self)!r})"

    __str__ = __repr__

