import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


import random
def rabin_karp(s, t):
    """
    ローリングハッシュ
    ハッシュ化にO(|S|+|T|)、検索にO(|S|)
    """
    def exe(x, m):
        th = 0
        for c in tt:
            th = (th * x + c) % m

        sh = 0
        for c in st[:l]:
            sh = (sh * x + c) % m
        xl = pow(x, l - 1, m)

        matched = set()
        if sh == th:
            matched.add(0)
        for i, (c0, c1) in enumerate(zip(st, st[l:]), start=1):
            sh = ((sh - c0 * xl) * x + c1) % m
            if sh == th:
                matched.add(i)

        return matched

    l = len(t)
    st = list(map(ord, s))
    tt = list(map(ord, t))
    # Xはなるべくst,ttの最大要素より大きくする
    # Mはとりあえず2^61-1(素数)を設定する
    xs = random.sample(range(10 ** 9, 10 ** 10), 3)
    ans = exe(xs[0], 2305843009213693951)
    ans.intersection_update(exe(xs[1], 2305843009213693951))
    ans.intersection_update(exe(xs[2], 2305843009213693951))
    return sorted(ans)


def manacher(s):
    """
    文字列Sから奇数長の最長の回文をO(|S|)で検索するアルゴリズム。
    Sの各文字の間にSには絶対に登場しないダミー文字を挟み込むと、偶数長の回文も見つけられる。
    両端と各文字の間に'$'を挿入すると、「各要素の値-1」がそこを中心とした回文の長さとなる。
    """
    n = len(s)
    radius = [0] * n
    i, j = 0, 0
    while i < n:
        while i - j >= 0 and i + j < n and s[i - j] == s[i + j]:
            j += 1
        radius[i] = j
        k = 1
        while i - k >= 0 and i + k < n and k + radius[i - k] < j:
            radius[i + k] = radius[i - k]
            k += 1
        i += k
        j -= k
    return radius



def main():
    pass


if __name__ == "__main__":
    main()