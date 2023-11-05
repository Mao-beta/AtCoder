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
EI = lambda m: [NLI() for _ in range(m)]


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
    N, M = NMI()
    B = [[]] + EI(M)
    ans = []
    for x in range(1, 201):
        # search x
        g = 0
        t = 0
        bi = 0
        for i in range(1, M+1):
            b = B[i]
            if x in b:
                t = b.index(x)
                if t == len(b)-1:
                    ans.append([x, 0])
                    b.pop()
                    break
                else:
                    # # 最も少ないところに置く
                    # g = 1
                    # sz = 1000
                    # for j in range(1, M+1):
                    #     if i == j:
                    #         continue
                    #     if len(B[j]) < sz:
                    #         sz = len(B[j])
                    #         g = j

                    # # 転倒数 + len(B[j])**2 が最小のところに置く
                    # tmp = b[t+1:]
                    # g = 1
                    # inv = 10000
                    # for j in range(1, M+1):
                    #     if i == j:
                    #         continue
                    #     n = inversion_num(B[j]+tmp[:]) + len(B[j]) ** 2
                    #     if n < inv:
                    #         g = j
                    #         inv = n

                    # 最小値が一番大きいところに置く
                    g = 1
                    min_num = 0
                    for j in range(1, M + 1):
                        if i == j:
                            continue
                        if B[j]:
                            tmpmax = min(B[j])
                        else:
                            tmpmax = 1000
                        if tmpmax > min_num:
                            min_num = tmpmax
                            g = j

                    ans.append([b[t+1], g])
                    ans.append([x, 0])
                    bi = i
                    break

        if g > 0:
            B[g] += B[bi][t+1:]
            B[bi] = B[bi][:t]

        # print(*B, sep="\n")

    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
