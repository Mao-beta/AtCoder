import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S), start=1):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


class BIT():
    def __init__(self, n):
        """
        1-index
        sum -> i番目までの和
        add -> i番目にxを足す
        :param n:
        """
        self.n = n
        self.data = [0] * (n + 1)
        self.each = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.each[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def __repr__(self):
        return str(self.each)


def inversion_num(A):
    """
    リストAの転倒数を座標圧縮ありで求める。要BIT, compress
    """
    N = len(A)
    Z, _ = compress(A)
    tree = BIT(N)
    res = 0
    for a in A:
        za = Z[a]
        res += tree.sum(za)
        tree.add(za, 1)
    return N * (N - 1) // 2 - res



def main():
    N = NI()
    P = NLI()

    Odd = [p % 2 for p in P]
    ans = []
    for i in range(N):
        # print(i, P[i], Odd)
        if i % 2 == 0:
            if P[i] % 2 == 1:
                Odd[i] = -1
                continue
            # 奇数番目に偶数がいる
            t = Odd.index(1)
            tt = t
            if (t - i) % 2:
                ans.append(f"A {t}")
                P[t-1], P[t] = P[t], P[t-1]
                t -= 1
            k = (t - i) // 2
            for _ in range(k):
                ans.append(f"B {t-1}")
                P[t - 2], P[t] = P[t], P[t - 2]
                t -= 2
            Odd[i] = -1
            Odd[tt] = 0

        if i % 2 == 1:
            if P[i] % 2 == 0:
                Odd[i] = -1
                continue
            # 偶数番目に奇数がいる
            t = Odd.index(0)
            tt = t
            if (t - i) % 2:
                ans.append(f"A {t}")
                P[t - 1], P[t] = P[t], P[t - 1]
                t -= 1
            k = (t - i) // 2
            for _ in range(k):
                ans.append(f"B {t-1}")
                P[t - 2], P[t] = P[t], P[t - 2]
                t -= 2
            Odd[i] = -1
            Odd[tt] = 1

    ODD = P[::2]
    EVEN = P[1::2]


    def bubble_sort(nlist, first):
        # 配列の要素数num
        num = len(nlist)
        ans = []

        for i in range(num):
            swap = False
            for j in range(num - 1, i, -1):
                # 後ろから順番に隣同士の要素を比較する
                if nlist[j - 1] > nlist[j]:
                    nlist[j - 1], nlist[j] = nlist[j], nlist[j - 1]
                    ans.append(j-1)
                    swap = True

            # 交換が行われなければ終了
            if swap == False:
                break

        ans = [f"B {a * 2 + first + 1}" for a in ans]

        return nlist, ans

    _, res_o = bubble_sort(ODD, 0)
    _, res_e = bubble_sort(EVEN, 1)

    ans += res_o + res_e
    print(len(ans))
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
