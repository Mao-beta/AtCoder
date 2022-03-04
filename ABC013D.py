import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

if "PyPy" in sys.version:
    import pypyjit

    pypyjit.set_param('max_unroll_recursion=-1')

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


class Doubling:
    def __init__(self, D, M=60):
        """Dが1回の遷移、2^M回までのダブリング表"""
        self.M = M
        self.D = [D]
        for m in range(self.M):
            tmp = []
            for i in range(len(D)):
                j = self.D[-1][i]
                tmp.append(self.D[-1][j])
            self.D.append(tmp)

    def pow(self, K, start):
        """ダブリング遷移DをもとにstartからK回後の遷移先を求める"""
        now = start
        for m in range(self.M):
            if (K >> m) & 1:
                now = self.D[m][now]
        return now


def main():
    N, M, D = NMI()
    A = NLI()
    move = list(range(N))
    for a in A[::-1]:
        a -= 1
        move[a], move[a+1] = move[a+1], move[a]

    # print(move)
    DBL = Doubling(move, 30)
    for i in range(N):
        print(DBL.pow(D, i)+1)


if __name__ == "__main__":
    main()
