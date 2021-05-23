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
    A = [i+a for i, a in enumerate(A)]
    B = [i+b for i, b in enumerate(B)]

    B_map = {}
    B_cnt = defaultdict(int)
    for i, b in enumerate(B, start=1):
        n = B_cnt[b]
        B_map[(b, n)] = i
        B_cnt[b] += 1

    bit = BIT(N)
    A_cnt = defaultdict(int)
    ans = 0
    for i, a in enumerate(A, start=1):
        n = A_cnt[a]
        try:
            idx = B_map[(a, n)]
        except:
            print(-1)
            exit()
        bit.add(idx, 1)
        ans += i - bit.sum(idx)
        A_cnt[a] += 1

    print(ans)




if __name__ == "__main__":
    main()
