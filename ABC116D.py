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


def main():
    N, K = NMI()
    sushis = [NLI() for _ in range(N)]
    sushis.sort(key=lambda x: -x[1])
    D = defaultdict(int)

    def rec(base, dic):
        pass

    print(sushis)






if __name__ == "__main__":
    main()