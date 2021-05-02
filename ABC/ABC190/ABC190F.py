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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


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
    bit = BIT(N)
    base = 0
    for i, a in enumerate(A, 0):
        a += 1
        base += i - bit.sum(a)
        bit.add(a, 1)
    print(base)
    for a in A[:-1]:
        base += N-1 - 2*a
        print(base)


if __name__ == "__main__":
    main()
