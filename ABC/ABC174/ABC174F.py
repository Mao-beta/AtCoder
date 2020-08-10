import sys
import math
from collections import defaultdict

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
        self.data = [0]*(n+1)
        self.each = [0]*(n+1)

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

    def __str__(self):
        return str(self.each)



def main():
    N, Q = NMI()
    C = [0]+NLI()
    d_querys = [[i]+NLI() for i in range(Q)]
    querys = defaultdict(list)
    for qi, ql, qr in d_querys:
        querys[qr].append((qi, ql))

    ans = [0] * Q
    last_index = [-1] * (N+1)
    index_dict = defaultdict(list)
    tree = BIT(N)

    for i, color in enumerate(C):
        if color == 0: continue
        idx = last_index[color]
        if idx != -1:
            index_dict[i].append((idx, i))
        last_index[color] = i
        tree.add(i, 1)

    for i in range(1, N+1):
        for idx, _ in index_dict[i]:
            tree.add(idx, -1)
        for qi, ql in querys[i]:
            ans[qi] = tree.sum(i) - tree.sum(ql-1)

    for a in ans:
        print(a)




if __name__ == "__main__":
    main()