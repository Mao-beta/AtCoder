import sys
import math
from collections import deque

# 再帰の深さ設定
sys.setrecursionlimit(1000000)
# 剰余初期化
MOD = 10 ** 9 + 7
MOD99 = 998244353
INF = 10 ** 20

# 入力
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

# アルファベットと数字の対応
alp_to_num = {chr(i+97): i for i in range(26)}
ALP_to_num = {chr(i+97).upper(): i for i in range(26)}
num_to_alp = {i: chr(i+97) for i in range(26)}
num_to_ALP = {i: chr(i+97).upper() for i in range(26)}


# 無限defaultdict
from collections import defaultdict
class recursiveDefaultdict(defaultdict):
    def __init__(self):
        super().__init__()
        self.default_factory = type(self)


def read_input_file(path):
    """
    pathのファイルをNLI()形式などでよみこむ
    """
    with open(path, mode="r") as f:
        A = [list(map(int, l.split())) for l in f.readlines()]
    #print(*A, sep="\n")


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


# グリッドの初期化　縦、横、初期値
def make_grid_int(h, w, num): return [[int(num)] * w for _ in range(h)]
def make_grid_bool(h, w, bool): return [[bool] * w for _ in range(h)]


# 隣接リスト
def adjlist(n, edges, first_idx=1, directed=False):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-first_idx, b-first_idx
        res[a].append(b)
        if not directed:
            res[b].append(a)
    return res


#隣接リスト 入力1-index を 0-index に
def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res

def adjlist_d_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
    return res

# 辺の端点からIDに紐づけする辞書
def edgedict_nond_1to0(edges):
    E_dic = {}
    for i, (u, v) in enumerate(edges):
        u, v = u-1, v-1
        E_dic[(u, v)] = i
        E_dic[(v, u)] = i
    return E_dic



class Knapsack:
    def __init__(self, N, WV):
        self.N = N
        self.WV = WV
        self.sumW = 0
        self.sumV = 0
        for w, v in WV:
            self.sumW += w
            self.sumV += v

    def solve_limW(self, limW):
        dp = [[0]*(limW + 1) for _ in range(self.N + 1)]

        for i in range(self.N):
            w, v = self.WV[i]
            for j in range(limW + 1):
                dp[i+1][j] = max(dp[i+1][j], dp[i][j])
                if j+w <= limW:
                    dp[i+1][j+w] = max(dp[i+1][j+w], dp[i][j] + v)

        return max(dp[-1])


class Doubling:
    def __init__(self, D, M=60):
        """Dが1回の遷移、2^M回までのダブリング表"""
        self.M = M
        self.D = [D]
        for m in range(self.M):
            tmp = []
            for i in range(len(D)):
                j = self.D[-1][i]
                tmp.append(self.D[-1][j])
            self.D.append(tmp)

    def pow(self, K, start):
        """ダブリング遷移DをもとにstartからK回後の遷移先を求める"""
        now = start
        for m in range(self.M):
            if (K >> m) & 1:
                now = self.D[m][now]
        return now



# ダブリングの骨格

def ide():
    """n==0や1などの終着点で返すもの"""
    return

def step(n):
    """nを1減らすとき"""
    return

def double(n):
    """nを半分にするとき"""
    return

from functools import lru_cache
@lru_cache(maxsize=None)
def rec(n):
    if n == 1:
        return ide()

    if n % 2:
        return step(rec(n-1))

    else:
        return double(rec(n//2))




def euler_tour(start, n, graph):
    """
    非再帰オイラーツアー
    :param start: 始点
    :param n: 頂点数
    :param graph: 隣接リスト(0-indexed)
    :return: 回った順の頂点のリスト
    """
    stack = deque()
    stack.append(start)

    seen = [0] * n
    seen[start] = 1
    res = []

    while stack:
        now = stack.pop()

        # 行きがけ
        if now >= 0:
            res.append(now)
            for goto in sorted(graph[now], reverse=True):
                if seen[goto]: continue
                seen[goto] = 1
                stack.append(~now) # ここ大事
                stack.append(goto)

        # 帰りがけ
        else:
            res.append(~now)

    return res


# grid探索セット
H = 10
W = 10
DIR = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def i2hw(i):
    return i//W, i%W

def hw2i(h, w):
    return h*W + w

def in_grid(h, w):
    return 0 <= h < H and 0 <= w < W

# バックトラックのようなもの
now = set()
grid = ["...."]*4

def rec(h, w):
    res = 0
    for dh, dw in DIR:
        nh, nw = h+dh, w+dw
        if not in_grid(nh, nw): continue
        if grid[nh][nw] == "#": continue
        if (nh, nw) in now: continue

        now.add((nh, nw))
        res = max(res, rec(nh, nw))
        now.discard((nh, nw))
    return res


# 半分全列挙
def split_and_list(A):
    """
    半分全列挙
    :param A: 長さ40以下くらいのList
    :return: 前半と後半それぞれについて、各部分集合の和のList
    """

    def solve_half(A_half):
        n = len(A_half)
        res = []
        for case in range(1<<n):
            now = 0
            for i in range(n):
                if (case >> i) & 1:
                    now += A_half[i]
            res.append(now)
        res.sort()
        return res

    N = len(A)
    return solve_half(A[:N//2]), solve_half(A[N//2:])




import bisect
def LIS(A):
    """
    A[:i]までに関するLISの長さのリストを取得する
    ans[i]はA[0:i+1]におけるLISの長さ
    """
    INF = 1<<60
    n = len(A)
    # dp[i]は長さがiとなるLISの末尾の最小値
    dp = [INF] * (n+1)
    dp[0] = -INF
    ans = []
    for a in A:
        idx = bisect.bisect_left(dp, a)
        dp[idx] = a
        ans.append(bisect.bisect_left(dp, INF) - 1)
    return ans


# dfs テンプレ
def dfs(start, graph):
    n = len(graph)
    stack = deque()
    stack.append(start)
    seen = [0] * n
    seen[start] = 1

    while stack:
        now = stack.pop()

        for goto in graph[now]:
            if seen[goto]:
                continue
            seen[goto] = 1
            stack.append(goto)

    return


def dfs_paint_01_color(start, graph):
    # 二色塗り分け
    from collections import deque

    stack = deque()
    stack.append(start)

    n = len(graph)
    colors = [-1] * n
    colors[start] = 0

    while stack:
        now = stack.pop()
        c = colors[now]

        for goto in graph[now]:
            if colors[goto] != -1:
                continue
            stack.append(goto)
            colors[goto] = 1 - c

    return colors



# K以下の積を満たす部分列の長さの最大値を得る尺取り法
def syakutori_mul(array, K):
    n = len(array)
    l, r = 0, 0
    mul = 1
    res = 0
    for l in range(n):
        while r < n and mul * array[r] <= K:
            mul *= array[r]
            r += 1
        res = max(res, r-l)
        if l == r:
            r += 1
        else:
            mul = mul // array[l]
    return res


# 狭義単調増加列のカウント
def syakutori_acc(array):
    n = len(array)
    r = 1
    res = 0
    for l in range(n):
        while 0 < r < n and (r <= l or array[r] > array[r-1]):
            r += 1
        res += r-l
        if l == r:
            r += 1

    return res


"""
# 尺取り法テンプレ
def syakutori(array):
    n = len(array)
    r = 1
    # 戻り値の初期値
    res = 0

    # 左端を全探索
    for l in range(n):
        # 頑張って右端を伸ばす部分 常に満たしたい条件をwhileで指定
        while 「満たしたい条件」:
            if r >= n:
                break
            r += 1

        # 区間の長さに応じて何かをする
        res += 「何らかの値」

        # 左端が追い付いたときに右端をずらす
        if l == r:
            r += 1

    return res
"""


""" 2**n bit全探索テンプレ
    for case in range(2**n):
        test = ""
        for i in range(n):
            if (case >> i) & 1:
                test = "1" + test
            else:
                test = "0" + test
        print(test)
"""

""" 幅優先探索テンプレ
    H, Wのgridで始点から終点までの歩数を数えるだけ
    要deque　壁は'#'
    
    H = 100
    W = 100
    start = (0, 0)

    queue = deque()
    queue.append(start)
    steps = [[-1] * W for _ in range(H)]
    steps[start[0]][start[1]] = 0

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        now_h, now_w = queue.popleft()
        now_step = steps[now_h][now_w]

        for dh, dw in dirs:
            goto_h = now_h + dh
            goto_w = now_w + dw
            goto_step = now_step + 1

            if goto_h < 0 or goto_h >= H or goto_w < 0 or goto_w >= W:
                continue
            if 0 <= steps[goto_h][goto_w] <= goto_step:
                continue
            if grid[goto_h][goto_w] == "#":
                continue

            queue.append((goto_h, goto_w))
            steps[goto_h][goto_w] = goto_step

    print(*steps, sep="\n")
"""



# 正方行列の積 mod
def mul_matrix(A, B, mod=10**9+7):
    size = len(A)
    ans = [[0] * size for _ in range(size)]
    for h in range(size):
        for w in range(size):
            for i in range(size):
                ans[h][w] += A[h][i] * B[i][w] % mod
                ans[h][w] %= mod
    return ans

# 正方行列の累乗 mod
def pow_matrix(A, n, mod=10**9+7):
    if n == 1:
        size = len(A)
        E = [[0] * size for _ in range(size)]
        for i in range(size):
            E[i][i] = 1
        return mul_matrix(A, E, mod)

    if n % 2 == 0:
        tA = pow_matrix(A, n//2, mod)
        return mul_matrix(tA, tA, mod)
    else:
        tA = pow_matrix(A, n-1, mod)
        return mul_matrix(tA, A, mod)


# 配列から累積和を返す
def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def transpose(A):
    """
    2次元list Aの転置行列
    """
    return [list(x) for x in zip(*A)]


def cum_2D(A):
    """
    2次元リストAの累積和（左と上は0になる）
    """
    H = len(A)
    W = len(A[0])
    C = [[0]*(W+1) for _ in range(H+1)]

    for h in range(H):
        cw = 0
        for w in range(W):
            cw += A[h][w]
            if h == 0 and w == 0:
                C[h+1][w+1] = A[h][w]
            elif h == 0:
                C[h+1][w+1] = A[h][w] + C[h+1][w]
            elif w == 0:
                C[h+1][w+1] = A[h][w] + C[h][w+1]
            else:
                C[h+1][w+1] = C[h][w+1] + cw

    return C


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]


class GridBit:
    """
    gridの状態をHW桁のbitで持つ 最低Ｏ(HW)はかかる
    bitが同じものは同一objectと判定される（setやdictに入れてよい）
    copyが出来ないので、bitの数値から復元するにはload_bitを使う
    1個ずつ操作するならset_one, set_zeroを使う
    """
    def __init__(self, H, W):
        self.bit = 0
        self.H = H
        self.W = W
        self.ones = set()

    def load_bit(self, bit):
        for i in range(self.H * self.W):
            if (bit>>i) & 1:
                h, w = self.i2hw(i)
                self.set_one(h, w)

    def one_num(self):
        return len(self.ones)

    def hw2i(self, h, w):
        return h * self.W + w

    def i2hw(self, i):
        return i//self.W, i%self.W

    def set_one(self, h, w):
        i = self.hw2i(h, w)
        self.bit |= 1<<i
        self.ones.add(i)

    def set_zero(self, h, w):
        i = self.hw2i(h, w)
        self.bit &= ~(1<<i)
        self.ones.discard(i)

    def is_one(self, h, w):
        i = self.hw2i(h, w)
        return (self.bit >> i) & 1

    def dir4(self, h, w):
        kouho = [[h-1, w], [h+1, w], [h, w-1], [h, w+1]]
        res = set()
        for nh, nw in kouho:
            if 0 <= nh < self.H and 0 <= nw < self.W:
                res.add(self.hw2i(nh, nw))
        return res


    def get_asides(self):
        """
        いま1のマスに隣接する0のマスの(h, w)を列挙する
        """
        res = set()
        for one in self.ones:
            oh, ow = self.i2hw(one)
            res |= self.dir4(oh, ow)
        res -= self.ones
        res = set([self.i2hw(x) for x in res])
        return res

    def __eq__(self, other):
        return self.bit == other.bit

    def __hash__(self):
        return hash(self.bit)

    def __repr__(self):
        str_b = bin(self.bit)[2:].zfill(self.H*self.W)[::-1]
        res = []
        for i in range(0, self.H*self.W, self.W):
            res.append(str_b[i: i+self.W])
        return "\n".join(res)



# 有理数クラス
class MyFraction:
    def __init__(self, a, b):
        assert b != 0, "分母が0です"

        if b < 0:
            a, b = -a, -b
        if a == 0:
            b = 1

        g = math.gcd(a, b)
        self.numerator = a // g
        self.denominator = b // g

    def __add__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = Fa_d * Fb_n + Fa_n * Fb_d
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __sub__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = - Fa_d * Fb_n + Fa_n * Fb_d
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __mul__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = Fa_n * Fb_n
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __truediv__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_d, Fb_n = other.get_nd()
        F_n = Fa_n * Fb_n
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __repr__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)


    def __lt__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        return Fa_n * Fb_d < Fb_n * Fa_d

    def __le__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        return Fa_n * Fb_d <= Fb_n * Fa_d

    def get_nd(self):
        return (self.numerator, self.denominator)


def z_algo(S):
    """
    長さNの文字列Sについて、各iに対し、 S と S[i:] の最長共通接頭辞を求める。
    O(N)
    """
    N = len(S)
    A = [0]*N
    i = 1; j = 0
    A[0] = l = len(S)
    while i < l:
        while i+j < l and S[j] == S[i+j]:
            j += 1
        if not j:
            i += 1
            continue
        A[i] = j
        k = 1
        while l-i > k < j - A[k]:
            A[i+k] = A[k]
            k += 1
        i += k; j -= k
    return A


def main():
    N = int()
    #A = list(map(int, input().split()))
    A = NLI()
    print(A)
    A = [[a, i] for i, a in enumerate(A, start=1)]
    A.sort(reverse=True)
    for a, i in A:
        print(i)


if __name__ == "__main__":
    main()