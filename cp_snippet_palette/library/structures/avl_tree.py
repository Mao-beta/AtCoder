"""非再帰AVL辞書。出典: _AVL_Tree.py。順位は0-indexed。更新・検索O(log n)。
PyPy向け。Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    avl = AVLTree()
    avl[20] = 'b'; avl[10] = 'a'
    avl[10], avl.kth(0), avl.ge(15), avl.lt(20)  # => ('a', 10, 20, 10)
    avl.get(99, 'missing')  # => 'missing'
    avl.discard(10), 10 in avl, len(avl)  # => (True, False, 1)
"""


class _AVLNode:
    """ノード

    Attributes:
        key (any): ノードのキー。比較可能なものであれば良い。(1, 4)などタプルも可。
        val (any): ノードの値。
        lch (Node): 左の子ノード。
        rch (Node): 右の子ノード。
        bias (int): 平衡度。(左部分木の高さ)-(右部分木の高さ)。
        size (int): 自分を根とする部分木の大きさ

    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.lch = None
        self.rch = None
        self.bias = 0
        self.size = 1


class AVLTree:
    """比較可能なキーを昇順に保持する辞書。AVLTree()は空。
    avl[key]=valueまたはset(key,val)で追加・上書き。avl[key]は未登録ならKeyError。get(key,default=None)は未登録ならdefault。
    kth(k)は小さい順0-indexedのキー、ge(x)はx以上の最小キー、lt(x)はx未満の最大キー。
    挿入・削除・探索O(log n)。len(avl)はキー数。同じキーの重複は持たない。
    引数なしで空の辞書をO(1)時間・空間で構築する。keyは相互に大小比較できるキー、valは任意の格納値。Nは現在のキー数。
    全体の空間O(N)、通常の探索・変更はO(log(N+1))時間。
    """

    def __init__(self):
        """引数なしで空の辞書をO(1)時間・空間で構築する。keyは相互に大小比較できるキー、valは任意の格納値。Nは現在のキー数。
        全体の空間O(N)、通常の探索・変更はO(log(N+1))時間。
        """
        self.root = None

    def _rotate_left(self, v):
        """内部用。部分木ノードvを左回転して新しい根ノードを返す。通常はset/discardを使う。
        vは内部ノードオブジェクト（キーや順位ではない）。内部補助処理でO(1)時間・空間。
        """
        u = v.rch
        u.size = v.size
        v.size -= u.rch.size + 1 if u.rch is not None else 1
        v.rch = u.lch
        u.lch = v
        if u.bias == -1:
            u.bias = v.bias = 0
        else:
            u.bias = 1
            v.bias = -1
        return u

    def _rotate_right(self, v):
        """内部用。部分木ノードvを右回転して新しい根ノードを返す。通常はset/discardを使う。
        vは内部ノードオブジェクト（キーや順位ではない）。内部補助処理でO(1)時間・空間。
        """
        u = v.lch
        u.size = v.size
        v.size -= u.lch.size + 1 if u.lch is not None else 1
        v.lch = u.rch
        u.rch = v
        if u.bias == 1:
            u.bias = v.bias = 0
        else:
            u.bias = -1
            v.bias = 1
        return u

    def _rotate_lr(self, v):
        """内部用。vに左・右の二重回転を適用し、新しい根ノードを返す。
        vは内部ノードオブジェクト（キーや順位ではない）。内部補助処理でO(1)時間・空間。
        """
        u = v.lch
        t = u.rch
        t.size = v.size
        v.size -= u.size - (t.rch.size if t.rch is not None else 0)
        u.size -= t.rch.size + 1 if t.rch is not None else 1
        u.rch = t.lch
        t.lch = u
        v.lch = t.rch
        t.rch = v
        self._update_bias_double(t)
        return t

    def _rotate_rl(self, v):
        """内部用。vに右・左の二重回転を適用し、新しい根ノードを返す。
        vは内部ノードオブジェクト（キーや順位ではない）。内部補助処理でO(1)時間・空間。
        """
        u = v.rch
        t = u.lch
        t.size = v.size
        v.size -= u.size - (t.lch.size if t.lch is not None else 0)
        u.size -= t.lch.size + 1 if t.lch is not None else 1
        u.lch = t.rch
        t.rch = u
        v.rch = t.lch
        t.lch = v
        self._update_bias_double(t)
        return t

    def _update_bias_double(self, v):
        """内部用。二重回転に必要な平衡係数を更新する。利用者からは呼ばない。
        vは内部ノードオブジェクト（キーや順位ではない）。内部補助処理でO(1)時間・空間。
        """
        if v.bias == 1:
            v.rch.bias = -1
            v.lch.bias = 0
        elif v.bias == -1:
            v.rch.bias = 0
            v.lch.bias = 1
        else:
            v.rch.bias = 0
            v.lch.bias = 0
        v.bias = 0

    def set(self, key, val):
        """挿入

        指定したkeyに値valを挿入する。
        その後、平衡を保つように回転を行う。

        Args:
            key (any): キー。
            val (any): 値。

        Note:
            同じキーがあった場合に上書きする。
        時間O(log(N+1))、追加空間O(log(N+1))以内。Nは現在のキー数。
        """
        if self.root is None:
            self.root = _AVLNode(key, val)
            return

        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lch
            elif v.key < key:
                history.append((v, -1))
                v = v.rch
            elif v.key == key:
                v.val = val
                return

        p, pdir = history[-1]
        if pdir == 1:
            p.lch = _AVLNode(key, val)
        else:
            p.rch = _AVLNode(key, val)

        while history:
            v, direction = history.pop()
            v.bias += direction
            v.size += 1

            new_v = None
            b = v.bias
            if b == 0:
                break

            if b == 2:
                u = v.lch
                if u.bias == -1:
                    new_v = self._rotate_lr(v)
                else:
                    new_v = self._rotate_right(v)
                break
            if b == -2:
                u = v.rch
                if u.bias == 1:
                    new_v = self._rotate_rl(v)
                else:
                    new_v = self._rotate_left(v)
                break

        if new_v is not None:
            if len(history) == 0:
                self.root = new_v
                return
            p, pdir = history.pop()
            p.size += 1
            if pdir == 1:
                p.lch = new_v
            else:
                p.rch = new_v

        while history:
            p, pdir = history.pop()
            p.size += 1

    def discard(self, key):
        """削除

        指定したkeyの要素を削除する。
        その後、平衡を保つように回転を行う。

        Args:
            key (any): キー。
            default: 未登録のときに返す値（省略時None）。

        Return:
            bool: 指定したキーが存在するならTrue、しないならFalse。
        時間O(log(N+1))、追加空間O(log(N+1))以内。Nは現在のキー数。
        """
        v = self.root
        history = []
        while v is not None:
            if key < v.key:
                history.append((v, 1))
                v = v.lch
            elif v.key < key:
                history.append((v, -1))
                v = v.rch
            else:
                break
        else:
            return False

        if v.lch is not None:
            history.append((v, 1))
            lmax = v.lch
            while lmax.rch is not None:
                history.append((lmax, -1))
                lmax = lmax.rch

            v.key = lmax.key
            v.val = lmax.val

            v = lmax

        c = v.rch if v.lch is None else v.lch

        if history:
            p, pdir = history[-1]
            if pdir == 1:
                p.lch = c
            else:
                p.rch = c
        else:
            self.root = c
            return True

        while history:
            new_p = None

            p, pdir = history.pop()
            p.bias -= pdir
            p.size -= 1

            b = p.bias
            if b == 2:
                if p.lch.bias == -1:
                    new_p = self._rotate_lr(p)
                else:
                    new_p = self._rotate_right(p)

            elif b == -2:
                if p.rch.bias == 1:
                    new_p = self._rotate_rl(p)
                else:
                    new_p = self._rotate_left(p)

            elif b != 0:
                break

            if new_p is not None:
                if len(history) == 0:
                    self.root = new_p
                    return True
                gp, gpdir = history[-1]
                if gpdir == 1:
                    gp.lch = new_p
                else:
                    gp.rch = new_p
                if new_p.bias != 0:
                    break

        while history:
            p, pdir = history.pop()
            p.size -= 1

        return True

    def __contains__(self, key):
        """キーの存在チェック

        指定したkeyがあるかどうか判定する。

        Args:
            key (any): キー。
            default: 未登録のときに返す値（省略時None）。

        Return:
            bool: 指定したキーが存在するならTrue、しないならFalse。
        時間O(log(N+1))、追加空間O(log(N+1))以内。Nは現在のキー数。
        """
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lch
            elif v.key < key:
                v = v.rch
            else:
                return True
        return False

    def get(self, key, default=None):
        """値の取り出し

        指定したkeyの値を返す。
        keyが存在しない場合はdefaultを返す。

        Args:
            key (any): キー。
            default: 未登録のときに返す値（省略時None）。

        Return:
            any: 指定したキーが存在するならその値、存在しないならdefault。
        時間O(log(N+1))、追加空間O(log(N+1))以内。Nは現在のキー数。
        """
        v = self.root
        while v is not None:
            if key < v.key:
                v = v.lch
            elif v.key < key:
                v = v.rch
            else:
                return v.val
        return default

    def ge(self, key):
        """下限つき探索

        指定したkey以上で最小のキーを見つける。

        Args:
            key (any): キーの下限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。
        時間O(log(N+1))、追加空間O(log(N+1))以内。Nは現在のキー数。
        """
        # ret = float('inf')
        ret = None
        v = self.root
        while v is not None:
            if v.key >= key:
                if ret is None or ret > v.key:
                    ret = v.key
                v = v.lch
            else:
                v = v.rch
        return ret

    def lt(self, key):
        """上限つき探索

        指定したkey未満で最大のキーを見つける。

        Args:
            key (any): キーの上限。

        Return:
            any: 条件を満たすようなキー。そのようなキーが一つも存在しないならNone。
        時間O(log(N+1))、追加空間O(log(N+1))以内。Nは現在のキー数。
        """
        # ret = -float('inf')
        ret = None
        v = self.root
        while v is not None:
            if v.key < key:
                if ret is None or ret < v.key:
                    ret = v.key
                v = v.rch
            else:
                v = v.lch
        return ret

    def kth(self, k):
        """小さい順0-indexedのk番目のキー。範囲外はIndexError。O(log n)。
        """
        if not 0 <= k < len(self):
            raise IndexError(k)
        v = self.root
        s = 0
        while v is not None:
            t = s + v.lch.size if v.lch is not None else s
            if t == k:
                return v.key
            elif t < k:
                s = t + 1
                v = v.rch
            else:
                v = v.lch
        return None


    def __getitem__(self, key):
        missing = object()
        value = self.get(key, missing)
        if value is missing:
            raise KeyError(key)
        return value

    def __setitem__(self, key, val):
        return self.set(key, val)

    def __delitem__(self, key):
        if not self.discard(key):
            raise KeyError(key)

    def __bool__(self):
        return self.root is not None

    def __len__(self):
        return self.root.size if self.root is not None else 0
