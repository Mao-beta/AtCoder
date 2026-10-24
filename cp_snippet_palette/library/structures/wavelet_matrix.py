"""静的な区間順位検索。添字・順位はすべて0-indexed、区間は[l,r)。

抽出元: _WaveletMatrix.py。提出時はこのファイルをコピーする（ローカルimport不要）。
PyPy向け。Codonでのコンパイルは未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    wm = WaveletMatrix([5, 1, 5, 3])
    wm.kth_smallest(0, 4, 1), wm.kth_largest(0, 4, 0)  # => (3, 5)
    wm.count(0, 3, 5), wm.count_less(0, 4, 4), wm.select(5, 1)  # => (2, 2, 2)
    wm.top(0, 4, 2), wm.sum(0, 4)  # => ([(5, 2), (1, 1)], 14)
    bits = FullyIndexableDictionary(4)
    bits.set(1, 1); bits.set(3, 1); bits.build()
    bits.rank(3, 1), bits.select(1, 1)  # => (1, 3)
"""


class FullyIndexableDictionary:
    """長さNの静的bit列。初期値は全て0。set(i,bit)を済ませてbuild()を1回呼ぶ。
    以後はget(index)/rank(index,bit)/select(bit,k)で参照する。添字・selectの順位は0-indexed。
    WaveletMatrixの補助構造。build後のsetは非対応。
    入力: Nは非負整数のbit数。構築O(ceil(N/32))時間・空間。
    index/iは0-indexedの添字、bitは0/1、kは0-indexed順位、defaultは見つからない場合の返り値。
    """

    def __init__(self, N):
        """入力: Nは非負整数のbit数。構築O(ceil(N/32))時間・空間。
        index/iは0-indexedの添字、bitは0/1、kは0-indexed順位、defaultは見つからない場合の返り値。
        """
        self.N = N
        self.blocks = (N + 31) >> 5
        self.bit = [0] * self.blocks
        self.total = [0] * self.blocks
        self.mask = [(1 << i) - 1 for i in range(1 << 5)]

    def __popcount(self, x):
        x = x - ((x >> 1) & 0x55555555)
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
        x = x + (x >> 4) & 0x0F0F0F0F
        x = x + (x >> 8)
        x = x + (x >> 16)
        return x & 0x0000007F

    def __len__(self):
        return self.N

    def set(self, index, bit):
        """第 index 要素を bit に設定する.
        時間・追加空間O(1)（32bitブロックを使う）。
        """
        if index < 0:
            index += self.N
        if not 0 <= index < self.N:
            raise IndexError(index)

        if bit:
            self.bit[index >> 5] |= 1 << (index & 31)
        else:
            self.bit[index >> 5] &= ~(1 << (index & 31))

    def build(self):
        """データ構造を確定させる. ※ 以降, set の使用禁止
        引数なし。時間O(ceil(N/32))、追加空間O(1)。
        """

        for k in range(1, self.blocks):
            self.total[k] = self.total[k - 1] + self.__popcount(self.bit[k - 1])

    def get(self, index):
        """第 index 要素の値を求める.
        時間・追加空間O(1)（32bitブロックを使う）。
        """
        if index < 0:
            index += self.N
        if not 0 <= index < self.N:
            raise IndexError(index)

        return (self.bit[index >> 5] >> (index & 31)) & 1

    __getitem__ = get

    def rank(self, index, bit):
        """[0, index) にある bit の数を求める.
        時間・追加空間O(1)（32bitブロックを使う）。
        """
        if index <= 0 or self.N == 0:
            return 0

        index = min(index, self.N)

        if index < self.N:
            alpha = self.total[index >> 5] + self.__popcount(
                self.bit[index >> 5] & self.mask[index & 31]
            )
        else:
            alpha = self.total[-1] + self.__popcount(self.bit[-1])
        return alpha if bit else index - alpha

    def select(self, bit, k, default=-1):
        """先頭からk番目のbitの位置を返す。k・返す位置は0-indexed。
        k=0は最初の出現。k<0または出現個数以上ならdefaultを返す。
        時間O(log(N+1))、追加空間O(1)。
        """
        if k < 0 or k >= self.rank(self.N, bit):
            return default

        l, r = 0, self.N
        while r - l > 1:
            m = (l + r) // 2
            if self.rank(m, bit) > k:
                r = m
            else:
                l = m
        return l


class WaveletMatrix:
    """静的な整数列Xから区間順位・頻度を検索する。負数・重複も座標圧縮して扱う。
    構築O(n log n)、基本的な検索はO(log σ)、σは異なる値の数。点更新は非対応。
    区間は[l,r)、kth_smallest/kth_largest/selectの順位kはすべて0-indexed。
    wm[i]で元の値、len(wm)で要素数を取得。sumは頻度列挙なので高速な区間和ではない。
    入力: Xは整数列（負数・重複も可）。N=len(X)、σ=len(set(X))、B=σ.bit_length()。
    構築O(N log(N+1))時間・O(N*(B+1))以内の空間。valueは元の整数値、各区間は0<=l<=r<=N。
    """
    def __init__(self, X):
        """入力: Xは整数列（負数・重複も可）。N=len(X)、σ=len(set(X))、B=σ.bit_length()。
        構築O(N log(N+1))時間・O(N*(B+1))以内の空間。valueは元の整数値、各区間は0<=l<=r<=N。
        """

        self.N = N = len(X)

        self.value_list = sorted(set(X))
        self.value_dict = {x: i for i, x in enumerate(self.value_list)}
        Y = [self.value_dict[x] for x in X]

        self.bit_size = len(self.value_dict).bit_length()
        self.max_value = (1 << self.bit_size) - 1

        self.zero_count = [0] * self.bit_size
        self.dict = [FullyIndexableDictionary(N) for _ in range(self.bit_size)]

        for lv in range(self.bit_size - 1, -1, -1):
            dic = self.dict[~lv]
            left = []
            right = []
            for i in range(N):
                if (Y[i] >> lv) & 1:
                    dic.set(i, 1)
                    right.append(Y[i])
                else:
                    left.append(Y[i])

            dic.build()
            self.zero_count[~lv] = len(left)

            Y = left + right

        self.begin = [0] * len(self.value_dict)
        for i in range(N - 1, -1, -1):
            self.begin[Y[i]] = i

    def get(self, index):
        """index 番目の要素を求める.

        index: 番号
        時間O(B+1)、追加空間O(1)。B=σ.bit_length()、σは異なる値数。
        indexは0-indexedの要素位置（負添字も可）。
        """

        if index < 0:
            index += self.N

        if not 0 <= index < self.N:
            raise IndexError(index)
        p = 0
        for lv in range(self.bit_size):
            dic = self.dict[lv]
            bit = dic.get(index)
            p = (p << 1) | bit

            if bit:
                index = self.zero_count[lv] + dic.rank(index, 1)
            else:
                index = dic.rank(index, 0)
        return self.value_list[p]

    __getitem__ = get

    def __len__(self):
        return self.N


    def count(self, l, r, value):
        """[l,r) にある value の個数を求める.

        l: 左端
        r: 右端 (第 r 項を含まない)
        value: 値
        時間O(B+1)、追加空間O(1)。B=σ.bit_length()、σは異なる値数。
        """

        if not 0 <= l <= r <= self.N:
            raise IndexError("invalid range")
        value = self.value_dict.get(value, -1)
        if value == -1:
            return 0

        for lv in range(self.bit_size):
            dic = self.dict[lv]
            if (value >> (self.bit_size - lv - 1)) & 1:
                l = dic.rank(l, 1) + self.zero_count[lv]
                r = dic.rank(r, 1) + self.zero_count[lv]
            else:
                l = dic.rank(l, 0)
                r = dic.rank(r, 0)

        return r - l

    def select(self, value, k, default=-1):
        """先頭からk番目に登場するvalueの位置を返す。k・返す位置は0-indexed。
        valueは元の整数値、k=0は最初の出現。k<0または出現個数以上ならdefault。
        時間O((B+1)*log(N+1))、追加空間O(1)。
        """

        if k < 0 or k >= self.count(0, self.N, value):
            return default
        value = self.value_dict.get(value, -1)
        if value == -1:
            return default

        p = self.begin[value]
        index = p + k

        for lv in range(self.bit_size):
            dic = self.dict[~lv]
            if (value >> lv) & 1:
                index = dic.select(1, index - self.zero_count[~lv])
            else:
                index = dic.select(0, index)
        return index

    def kth_smallest(self, l, r, k):
        """[l,r)の小さい方からk番目の値。kは0-indexed（0が最小）。
        0<=k<r-l。範囲外はIndexError。
        時間O(B+1)、追加空間O(1)。B=σ.bit_length()、σは異なる値数。
        """

        if not (0 <= l <= r <= self.N and 0 <= k < r - l):
            raise IndexError("invalid range or rank")
        p = 0
        for lv in range(self.bit_size):
            dic = self.dict[lv]
            alpha = dic.rank(r, 0) - dic.rank(l, 0)
            p <<= 1
            if alpha <= k:
                p |= 1
                k -= alpha
                l = dic.rank(l, 1) + self.zero_count[lv]
                r = dic.rank(r, 1) + self.zero_count[lv]
            else:
                l = dic.rank(l, 0)
                r = dic.rank(r, 0)
        return self.value_list[p]



    def count_less(self, l, r, value):
        """[l,r)内でvalue未満の個数。O(log σ)。
        時間O(B+1)、追加空間O(1)。B=σ.bit_length()、σは異なる値数。
        """
        from bisect import bisect_left

        if not 0 <= l <= r <= self.N:
            raise IndexError("invalid range")
        bound = bisect_left(self.value_list, value)
        if bound == len(self.value_list):
            return r - l
        answer = 0
        for level, dic in enumerate(self.dict):
            l0, r0 = dic.rank(l, 0), dic.rank(r, 0)
            if (bound >> (self.bit_size - level - 1)) & 1:
                answer += r0 - l0
                l = self.zero_count[level] + l - l0
                r = self.zero_count[level] + r - r0
            else:
                l, r = l0, r0
        return answer

    def kth_largest(self, l, r, k):
        """[l,r)の大きい方からk番目の値。kは0-indexed（0が最大）。
        0<=k<r-l。範囲外はIndexError。
        時間O(B+1)、追加空間O(1)。B=σ.bit_length()、σは異なる値数。
        """
        return self.kth_smallest(l, r, r - l - 1 - k)

    def top(self, l, r, k):
        """[l,r) にある出現回数が多い順から k 個 (値, 個数) のタプルを出力する (個数同率は値が小さい方が優先).

        l: 左端
        r: 右端 (第 r 項を含まない)
        k: 採用する要素数
        kは出力する異なる値の最大個数の非負整数。訪問する二分木ノード数をTとするとO(T log(T+1))時間・O(T)空間。
        Tは最大O(σ*(B+1))以内で、kだけでは時間を決められない。
        """
        if not 0 <= l <= r <= self.N or k < 0:
            raise IndexError("invalid range or count")
        if l == r or k == 0:
            return []

        from heapq import heappush, heappop

        X = []
        Q = [(-(r - l), 0, 0, l, r)]
        while k and Q:
            _, value, lv, l, r = heappop(Q)

            if lv == self.bit_size:
                X.append((self.value_list[value], r - l))
                k -= 1
            else:
                dic = self.dict[lv]
                beta = dic.rank(l, 0)
                alpha = dic.rank(r, 0) - beta

                # 0
                if alpha > 0:
                    heappush(Q, (-alpha, value << 1, lv + 1, beta, beta + alpha))

                # 1
                if (r - l) - alpha > 0:
                    x = self.zero_count[lv] + (l - beta)
                    y = x + (r - l - alpha)
                    heappush(Q, (-((r - l) - alpha), (value << 1) | 1, lv + 1, x, y))
        return X

    def sum(self, l, r):
        """[l,r)の値の総和。空なら0。
        異なる値の頻度をtopで列挙して計算するためO(log σ)ではない。
        和だけを多数問う場合は累積和を併用する。
        topで訪問するノード数Tに対しO(T log(T+1))時間・O(T)空間。区間長にかかわらずO(log σ)になる実装ではない。
        """
        X = 0
        for x, f in self.top(l, r, r - l):
            X += x * f
        return X

    def intersect(self, l1, r1, l2, r2):
        """[l1, r1), [l2, r2) に共に存在する要素 v における (v, 1番目の区間にある v  の個数, 2番目の区間にある v  の個数) のリストを出力する.
        l1/r1とl2/r2はそれぞれ0<=l<=r<=Nの半開区間境界。訪問ノード数Tに対してO(T)時間・空間、Tは最大O(σ*(B+1))以内。
        """
        X = [(l1, r1, l2, r2, 0)]
        for lv in range(self.bit_size):
            Y = X
            X = []
            dic = self.dict[lv]
            for l1, r1, l2, r2, value in Y:
                beta1 = dic.rank(l1, 0)
                alpha1 = dic.rank(r1, 0) - beta1
                a1 = beta1
                b1 = beta1 + alpha1
                c1 = self.zero_count[lv] + (l1 - beta1)
                d1 = c1 + (r1 - l1 - alpha1)

                beta2 = dic.rank(l2, 0)
                alpha2 = dic.rank(r2, 0) - beta2
                a2 = beta2
                b2 = beta2 + alpha2
                c2 = self.zero_count[lv] + (l2 - beta2)
                d2 = c2 + (r2 - l2 - alpha2)

                if a1 < b1 and a2 < b2:
                    X.append((a1, b1, a2, b2, value << 1))

                if c1 < d1 and c2 < d2:
                    X.append((c1, d1, c2, d2, (value << 1) | 1))

        return [
            (self.value_list[value], y1 - x1, y2 - x2) for x1, y1, x2, y2, value in X
        ]
