import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class BIT():
    def __init__(self, n):
        """
        1-index
        sum -> i番目までの和
        add -> i番目にxを足す
        update -> i番目をxにする
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

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l)

    def add(self, i, x):
        self.each[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def update(self, i, x):
        prev = self.each[i]
        gap = x - prev
        self.add(i, gap)

    def __repr__(self):
        return str(self.each)


def main():
    N, M, Q = NMI()
    querys = [NLI() for _ in range(Q)]
    Ys = [0] + [y for _, _, y in querys]

    def compress(S):
        """ 座標圧縮 """
        zipped, unzipped = {}, {}
        for i, a in enumerate(sorted(S), start=1):
            zipped[a] = i
            unzipped[i] = a
        return zipped, unzipped

    zip_y, unzip_y = compress(set(Ys))
    #print(zip_y)

    BIT_len = len(zip_y) + 5
    #print(BIT_len)

    A = [0] * (N+1)
    B = [0] * (M+1)
    A_cnt = BIT(BIT_len)
    B_cnt = BIT(BIT_len)
    A_sum = BIT(BIT_len)
    B_sum = BIT(BIT_len)

    A_cnt.update(1, N)
    B_cnt.update(1, M)

    ans = 0
    for T, X, Y in querys:
        if T == 1:
            y = A[X]
            A[X] = Y
            zy, ZY = zip_y[y], zip_y[Y]

            ans -= y * B_cnt.sum(zy) + (B_sum.sum(BIT_len) - B_sum.sum(zy))
            ans += Y * B_cnt.sum(ZY) + (B_sum.sum(BIT_len) - B_sum.sum(ZY))

            A_cnt.add(zy, -1)
            A_cnt.add(ZY, 1)
            A_sum.add(zy, -y)
            A_sum.add(ZY, Y)

        else:
            y = B[X]
            B[X] = Y
            zy, ZY = zip_y[y], zip_y[Y]

            ans -= y * A_cnt.sum(zy) + (A_sum.sum(BIT_len) - A_sum.sum(zy))
            ans += Y * A_cnt.sum(ZY) + (A_sum.sum(BIT_len) - A_sum.sum(ZY))

            B_cnt.add(zy, -1)
            B_cnt.add(ZY, 1)
            B_sum.add(zy, -y)
            B_sum.add(ZY, Y)

        print(ans)



if __name__ == "__main__":
    main()
