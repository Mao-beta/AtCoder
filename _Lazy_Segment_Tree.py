import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class lazy_segtree:
    # 遅延評価セグメント木
    def __init__(s, op, e, mapping, composition, id, v):
        if type(v) is int: v = [e()] * v
        s._n = len(v)
        s.log = s.ceil_pow2(s._n)
        s.size = 1 << s.log
        s.d = [e()] * (2 * s.size)
        s.lz = [id()] * s.size
        s.e = e
        s.op = op
        s.mapping = mapping
        s.composition = composition
        s.id = id
        for i in range(s._n): s.d[s.size + i] = v[i]
        for i in range(s.size - 1, 0, -1): s.update(i)

    # 1点更新
    def set(s, p, x):
        p += s.size
        for i in range(s.log, 0, -1): s.push(p >> i)
        s.d[p] = x
        for i in range(1, s.log + 1): s.update(p >> i)

    # 1点取得
    def get(s, p):
        p += s.size
        for i in range(s.log, 0, -1): s.push(p >> i)
        return s.d[p]

    # 区間演算
    def prod(s, l, r):
        if l == r: return s.e()
        l += s.size
        r += s.size
        for i in range(s.log, 0, -1):
            if (((l >> i) << i) != l): s.push(l >> i)
            if (((r >> i) << i) != r): s.push(r >> i)
        sml, smr = s.e(), s.e()
        while (l < r):
            if l & 1:
                sml = s.op(sml, s.d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = s.op(s.d[r], smr)
            l >>= 1
            r >>= 1
        return s.op(sml, smr)

    # 全体演算
    def all_prod(s):
        return s.d[1]

    # 1点写像
    def apply(s, p, f):
        p += s.size
        for i in range(s.log, 0, -1): s.push(p >> i)
        s.d[p] = s.mapping(f, s.d[p])
        for i in range(1, s.log + 1): s.update(p >> i)

    # 区間写像
    def apply(s, l, r, f):
        if l == r: return
        l += s.size
        r += s.size
        for i in range(s.log, 0, -1):
            if (((l >> i) << i) != l): s.push(l >> i)
            if (((r >> i) << i) != r): s.push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                sml = s.all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                smr = s.all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, s.log + 1):
            if (((l >> i) << i) != l): s.update(l >> i)
            if (((r >> i) << i) != r): s.update((r - 1) >> i)

    # L固定時の最長区間のR
    def max_right(s, l, g):
        if l == s._n: return s._n
        l += s.size
        for i in range(s.log, 0, -1): s.push(l >> i)
        sm = s.e()
        while True:
            while (l % 2 == 0): l >>= 1
            if not g(s.op(sm, s.d[l])):
                while l < s.size:
                    s.push(l)
                    l = 2 * l
                    if g(s.op(sm, s.d[l])):
                        sm = s.op(sm, s.d[l])
                        l += 1
                return l - s.size
            sm = s.op(sm, s.d[l])
            l += 1
            if (l & -l) == l: break
        return s._n

    # R固定時の最長区間のL
    def min_left(s, r, g):
        if r == 0: return 0
        r += s.size
        for i in range(s.log, 0, -1): s.push((r - 1) >> i)
        sm = s.e()
        while True:
            r -= 1
            while r > 1 and (r % 2): r >>= 1
            if not g(s.op(s.d[r], sm)):
                while r < s.size:
                    s.push(r)
                    r = 2 * r + 1
                    if g(s.op(s.d[r], sm)):
                        sm = s.op(s.d[r], sm)
                        r -= 1
                return r + 1 - s.size
            sm = s.op(s.d[r], sm)
            if (r & - r) == r: break
        return 0

    def update(s, k):
        s.d[k] = s.op(s.d[2 * k], s.d[2 * k + 1])

    def all_apply(s, k, f):
        s.d[k] = s.mapping(f, s.d[k])
        if k < s.size: s.lz[k] = s.composition(f, s.lz[k])

    def push(s, k):
        s.all_apply(2 * k, s.lz[k])
        s.all_apply(2 * k + 1, s.lz[k])
        s.lz[k] = s.id()

    def ceil_pow2(s, n):
        x = 0
        while (1 << x) < n: x += 1
        return x


INF = 10**20
# opの恒等写像
def e():
    return INF

# ノード間演算(prodなど)
def op(s, t):
    return min(s, t)

# 各ノードに対する更新作用(applyなど)
def mapping(f, a):
    return f + a

# f(g())の合成写像
def composition(f, g):
    return f + g

# mappingの恒等写像
def id():
    return 0


def main():
    N, M = NMI()
    querys = [NLI() for _ in range(M)]

    tree = lazy_segtree(op, e, mapping, composition, id, N)

    for i in range(N):
        tree.set(i, 0)

    for s, t in querys:
        s, t = s-1, t-1
        tree.apply(s, t+1, 1)

    ans = []
    for i, (s, t) in enumerate(querys, start=1):
        s, t = s-1, t-1
        m = tree.prod(s, t+1)
        if m > 1:
            ans.append(i)

    print(len(ans))
    if ans:
        print(*ans, sep="\n")


if __name__ == "__main__":
    main()



"""
区間加算、区間最小値取得
INF = 10**20
# opの恒等写像
def e():
    return INF

# ノード間演算(prodなど)
def op(s, t):
    return min(s, t)

# 各ノードに対する更新作用(applyなど)
def mapping(f, a):
    return f + a

# f(g())の合成写像
def composition(f, g):
    return f + g

# mappingの恒等写像
def id():
    return 0
"""


"""
区間更新、区間最大値取得
INF = 10**10
ID = 10**10

# opの恒等写像
def e():
    return -INF

# ノード間演算(prodなど)
def op(s, t):
    return max(s, t)

# 各ノードに対する更新作用(applyなど)
# 区間加算ならfに足す値、aに足される値が来る
def mapping(f, a):
    return a if f == ID else f

# f(g())の合成写像
def composition(f, g):
    return g if f == ID else f

# mappingの恒等写像
def id():
    return ID
"""


"""
# 区間更新・区間加算(10進法でそのまま表示)
MOD = 998244353

INF = 1<<60

max_N = 200003
ten = [pow(10, i, MOD) for i in range(max_N)]
one = [0]
for i in range(max_N-1):
    one.append((one[-1]*10+1)%MOD)

def S(_sum, _len):
    return (_sum << 30) + _len

def S2sum(s):
    return s >> 30

def S2len(s):
    return s & ((1<<30) - 1)


# opの恒等写像
def e():
    return S(0, 0)

# ノード間演算(prodなど)
def op(s, t):
    res_sum = (S2sum(s) * ten[S2len(t)] + S2sum(t)) % MOD
    res_len = (S2len(s) + S2len(t)) % MOD
    return S(res_sum, res_len)

# 各ノードに対する更新作用(applyなど)
# 区間加算ならfに足す値、aに足される値が来る
def mapping(f, a):
    if f == 0:
        return a
    return S(f * one[S2len(a)], S2len(a))


# f(g())の合成写像
def composition(f, g):
    return g if f == 0 else f

# mappingの恒等写像
def id():
    return 0
    
"""