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


from pathlib import Path
from random import randint

IS_LOCAL = True
try:
    import seaborn
except:
    IS_LOCAL = False


class Judge:
    def __init__(self, N, D, Q, W):
        self.N, self.D, self.Q, self.W = N, D, Q, W
        self.judged = [0] * self.N
        self.win = [0] * self.N

    def query(self, L, R):
        assert self.Q > 0
        self.Q -= 1
        print(len(L), len(R), *L, *R, flush=True)
        if IS_LOCAL:
            LW = sum([self.W[i] for i in L])
            RW = sum([self.W[i] for i in R])
            if LW > RW:
                res = ">"
            elif LW < RW:
                res = "<"
            else:
                res = "="
        else:
            res = SI()

        for i in L+R:
            self.judged[i] += 2

        if res == ">":
            for i in L:
                self.win[i] += 2
        elif res == "<":
            for i in R:
                self.win[i] += 2
        else:
            for i in L+R:
                self.win[i] += 1

        return res

    def ratio(self, i):
        # i番目のwin/judgedを返す(judged=0なら0)
        if self.judged[i] == 0:
            return 0
        else:
            return self.win[i] / self.judged[i]


class Solver:
    def __init__(self, N, D, Q, W, judge: Judge):
        self.N, self.D, self.Q, self.W = N, D, Q, W
        self.firstQ = Q
        self.ans = [0] * N
        self.Data = [[] for _ in range(D)]
        for i in range(N):
            self.Data[i % D].append(i)
            self.ans[i] = i % D

        self.judge = judge


    def visualize(self):
        print("#c", *self.ans, flush=True)

    def output_ans(self):
        print(*self.ans, flush=True)

    def compare_all(self):
        # D組全体のバブルソート D(D-1)/2回の比較
        need = self.D * (self.D - 1) // 2
        if self.Q < need:
            for i in range(self.Q):
                self.judge.query(self.Data[0], self.Data[1])
            self.Q = 0
            return

        cnt = 0
        for i in range(self.D):
            for j in range(0, self.D - i - 1):
                # f(Li, Lj)がTrueの場合、スワップ
                cnt += 1
                if self.judge.query(self.Data[j], self.Data[j + 1]) == ">":
                    self.Data[j], self.Data[j + 1] = self.Data[j + 1], self.Data[j]

        self.Q -= need

    def compare_after_swap(self):
        # 前からと後ろから2周だけ比較
        # swapしなかったらその周はおわり
        for j in range(0, self.D - 1):
            if self.Q <= 0:
                break
            self.Q -= 1
            # f(Li, Lj)がTrueの場合、スワップ
            if self.judge.query(self.Data[j], self.Data[j + 1]) == ">":
                self.Data[j], self.Data[j + 1] = self.Data[j + 1], self.Data[j]
            else:
                break

        for j in range(self.D - 2, -1, -1):
            if self.Q <= 0:
                break
            self.Q -= 1
            # f(Li, Lj)がTrueの場合、スワップ
            if self.judge.query(self.Data[j], self.Data[j + 1]) == ">":
                self.Data[j], self.Data[j + 1] = self.Data[j + 1], self.Data[j]
            else:
                break

    def swap(self, d1, i1, d2, i2):
        v1 = self.Data[d1][i1]
        v2 = self.Data[d2][i2]
        self.ans[v1], self.ans[v2] = self.ans[v2], self.ans[v1]
        self.Data[d1][i1], self.Data[d2][i2] = self.Data[d2][i2], self.Data[d1][i1]

    def swap_min_one_and_max_one(self):
        # Dataはsort済みとする
        minidx = randint(0, len(self.Data[0])-1)
        maxidx = randint(0, len(self.Data[-1]) - 1)
        self.swap(0, minidx, -1, maxidx)

    def data_sort(self):
        for data in self.Data:
            data.sort(key=lambda x: self.judge.ratio(x))

    def swap_ratios(self):
        self.data_sort()
        max_cutoff = int((len(self.Data[-1])-1) * self.Q / self.firstQ)
        self.swap(0, 0, -1, max_cutoff)

def solve(N, D, Q, W):
    judge = Judge(N, D, Q, W)
    solver = Solver(N, D, Q, W, judge)
    print("#", solver.N, solver.D, solver.Q)
    solver.compare_all()
    solver.visualize()
    while solver.Q > 0:
        # solver.swap_min_one_and_max_one()
        solver.swap_ratios()
        solver.compare_after_swap()
        solver.visualize()
        print("#", solver.N, solver.D, solver.Q)

    assert len(solver.ans) == solver.N
    solver.output_ans()

def main():
    if IS_LOCAL:
        in_files = sorted(list(Path("./in/").glob("*.txt")))

        Inputs = []
        for p in in_files:
            with open(p, mode="r") as f:
                N, D, Q = map(int, f.readline().split())
                W = list(map(int, f.readline().split()))
                Inputs.append([N, D, Q, W])

        for i, (N, D, Q, W) in enumerate(Inputs):
            if i == 1:
                solve(N, D, Q, W)

    else:
        N, D, Q = NMI()
        solve(N, D, Q, None)


if __name__ == "__main__":
    main()
