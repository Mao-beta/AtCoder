"""競プロ用スニペット。単体で貼り付け可能。2026-10-17版。"""

class Deque:
    """リングバッファによる両端キュー。整数添字でのランダムアクセス O(1)。

    Deque(src_arr=None, max_size=8)。max_size は初期予約容量（上限ではない）。
    append/appendleft/pop/popleft は償却 O(1)、添字取得・代入 O(1)。
    extend と走査は O(k)、rotate は O(min(k mod N, N-k mod N))。
    必要時に容量を倍増させる。大容量の事前確保が必要なら max_size を指定。
    """

    def __init__(self, src_arr=None, max_size=8):
        arr = [] if src_arr is None else list(src_arr)
        self.N = max(1, max_size, len(arr))
        self.buf = arr + [None] * (self.N - len(arr))
        self.head = 0
        self._size = len(arr)
        self.tail = self._size % self.N

    def __len__(self):
        return self._size

    def is_full(self):
        return self._size == self.N

    def is_empty(self):
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
        if self.is_full():
            self.__grow()
        self.buf[self.tail] = x
        self.tail = (self.tail + 1) % self.N
        self._size += 1

    def appendleft(self, x):
        if self.is_full():
            self.__grow()
        self.head = (self.head - 1) % self.N
        self.buf[self.head] = x
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        self.tail = (self.tail - 1) % self.N
        x = self.buf[self.tail]
        self.buf[self.tail] = None
        self._size -= 1
        return x

    def popleft(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        x = self.buf[self.head]
        self.buf[self.head] = None
        self.head = (self.head + 1) % self.N
        self._size -= 1
        return x

    def extend(self, iterable):
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable):
        for x in iterable:
            self.appendleft(x)

    def rotate(self, k=1):
        """右に k 個回転。負数は左回転。"""
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

