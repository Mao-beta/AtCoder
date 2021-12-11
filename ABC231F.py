import sys
import math
from collections import defaultdict

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
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


def main():
    N = NI()
    A = NLI()
    B = NLI()
    AB = [[a, b] for a, b in zip(A, B)]
    AB.sort(key=lambda x: (x[0], -x[1]))
    ZB, UZB = compress(B)
    ZNB = len(ZB)

    Dup = defaultdict(int)
    for a, b in AB:
        Dup[(a, b)] += 1

    tree = BIT(ZNB)
    ans = 0
    for a, b in AB:
        zb = ZB[b]
        tree.add(zb + 1, 1)
        ans += tree.sum(ZNB) - tree.sum(zb)

    for x in Dup.values():
        x -= 1
        ans += x*(x+1)//2

    print(ans)


if __name__ == "__main__":
    main()
