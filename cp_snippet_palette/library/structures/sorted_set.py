"""順序付き集合・多重集合。添字は0-indexed。更新・順位取得はO(sqrt(n))。

抽出元: _Sorted_Set.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    s = SortedSet([3, 1, 3])
    list(s), s[0], s.ge(2), s.bisect_left(3)  # => ([1, 3], 1, 3, 1)
    s.add(2), s.discard(9)  # => (True, False)
    m = SortedMultiset([3, 1, 3])
    m.count(3), m[2], m.bisect_right(3)  # => (2, 3, 3)
"""

import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

T = TypeVar("T")


class SortedSet(Generic[T]):
    """比較可能な値の順序付き集合。初期値・追加値の重複を除く。
    aは初期要素のiterable（省略時は空）。s[k]は小さい順0-indexed、負添字も可。
    len(s)、x in s、list(s)（昇順）、reversed(s)が使える。更新・順位操作O(√n)。
    入力: aは相互に大小比較可能な要素のiterable（省略は空）。Nは初期要素数、nは操作時の要素数。
    構築は整列済みならO(N)、それ以外O(N log(N+1))時間、空間O(N)。xは検索/更新する値。更新・順位取得のO(sqrt(n))は償却の目安で、再構築単発はO(n)。
    """
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [
            a[size * i // bucket_size : size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __init__(self, a: Iterable[T] = ()) -> None:
        """入力: aは相互に大小比較可能な要素のiterable（省略は空）。Nは初期要素数、nは操作時の要素数。
        構築は整列済みならO(N)、それ以外O(N log(N+1))時間、空間O(N)。xは検索/更新する値。更新・順位取得のO(sqrt(n))は償却の目安で、再構築単発はO(n)。
        """
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        """xを追加できたらTrue、既存ならFalse。O(√n)。
        """
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        """xを1個削除できたらTrue、なければFalse。O(√n)。
        """
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x:
            return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0:
            self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        """x未満の最大の値を返す。存在しなければNone。O(√n)。
        """
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        """x以下の最大の値を返す。存在しなければNone。O(√n)。
        """
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        """xを超える最小の値を返す。存在しなければNone。O(√n)。
        """
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        """x以上の最小の値を返す。存在しなければNone。O(√n)。
        """
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError
        for a in self.a:
            if x < len(a):
                return a[x]
            x -= len(a)
        raise IndexError

    def bisect_left(self, x: T) -> int:
        """x未満の要素数を返す。x自体が未登録でもよい。O(√n)。
        """
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def bisect_right(self, x: T) -> int:
        """x以下の要素数を返す。x自体が未登録でもよい。O(√n)。
        """
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


class SortedMultiset(Generic[T]):
    """比較可能な値の順序付き多重集合。重複を保持する。
    aは初期要素のiterable（省略時は空）。s[k]は小さい順0-indexed、負添字も可。
    len(s)、x in s、list(s)（昇順）、reversed(s)が使える。更新・順位操作O(√n)。
    入力: aは相互に大小比較可能な要素のiterable（省略は空）。Nは初期要素数、nは操作時の要素数。
    構築は整列済みならO(N)、それ以外O(N log(N+1))時間、空間O(N)。xは検索/更新する値。更新・順位取得のO(sqrt(n))は償却の目安で、再構築単発はO(n)。
    """
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [
            a[size * i // bucket_size : size * (i + 1) // bucket_size]
            for i in range(bucket_size)
        ]

    def __init__(self, a: Iterable[T] = ()) -> None:
        """入力: aは相互に大小比較可能な要素のiterable（省略は空）。Nは初期要素数、nは操作時の要素数。
        構築は整列済みならO(N)、それ以外O(N log(N+1))時間、空間O(N)。xは検索/更新する値。更新・順位取得のO(sqrt(n))は償却の目安で、再構築単発はO(n)。
        """
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        """xの出現数を返す。未登録なら0。O(√n)。
        """
        return self.bisect_right(x) - self.bisect_left(x)

    def add(self, x: T) -> None:
        """xを追加する。戻り値なし。重複も1個として保持。O(√n)。
        """
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        """xを1個削除できたらTrue、なければFalse。O(√n)。
        """
        if self.size == 0:
            return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x:
            return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0:
            self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        """x未満の最大の値を返す。存在しなければNone。O(√n)。
        """
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        """x以下の最大の値を返す。存在しなければNone。O(√n)。
        """
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        """xを超える最小の値を返す。存在しなければNone。O(√n)。
        """
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        """x以上の最小の値を返す。存在しなければNone。O(√n)。
        """
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError
        for a in self.a:
            if x < len(a):
                return a[x]
            x -= len(a)
        raise IndexError

    def bisect_left(self, x: T) -> int:
        """x未満の要素数を返す。x自体が未登録でもよい。O(√n)。
        """
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def bisect_right(self, x: T) -> int:
        """x以下の要素数を返す。x自体が未登録でもよい。O(√n)。
        """
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans
