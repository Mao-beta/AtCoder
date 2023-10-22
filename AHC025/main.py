import random
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


def solve_randommatch(N, D, Q, W, root=None, f=None):

    judge = Judge(N, D, Q, W)
    if root is None:
        root = int(N ** 0.5)

    # r個ずつ適当に比較を繰り返してスコアをためる
    IDs = list(range(N))
    counts = [0] * N

    # 1週目は全部使う
    first_IDs = list(range(N)) * 2
    for i in range((N+2*root-1)//(2*root)):
        L = first_IDs[2 * root * i: 2 * root * i + root]
        R = first_IDs[2 * root * i + root: 2 * root * i + 2 * root]
        judge.query(L, R)
        for idx in L + R:
            counts[idx] += 1

    while judge.Q > 0:
        L = random.sample(IDs, root)
        rem = set(IDs) - set(L)
        R = random.sample(rem, root)
        judge.query(L, R)
        for idx in L+R:
            counts[idx] += 1

    Y = [win / c for c, win in zip(counts, judge.win)]

    def expected_value_of_rank(rank, N, lambda_val):
        K = rank + 1  # rankは0から始まるため、Kはrank + 1
        return sum(1 / (N - i) for i in range(K)) / lambda_val

    def expected_values_of_ranks(ranks, N, lambda_val=1e-5):
        return [expected_value_of_rank(rank, N, lambda_val) for rank in ranks]

    E = expected_values_of_ranks(list(range(N)), N)

    YI = [[y, i] for i, y in enumerate(Y)]
    YI.sort()
    estimated = [[E[r], i] for r, (y, i) in enumerate(YI)]
    EW = [0] * N
    for e, i in estimated:
        EW[i] = e



    if IS_LOCAL:
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.scatterplot(x=W, y=EW)
        sns.lineplot(x=[0, max(W+EW)], y=[0, max(W+EW)], c="r")
        path = Path("./randommatch") / ("WvsEW_" + f)
        title = f"{path.stem}.txt, N: {N}, D: {D}, Q: {Q}, itr: {round(sum(counts) / N)}"
        plt.title(title)
        plt.tight_layout()
        plt.savefig(path)
        plt.close()




    def greedy_partition(W, D):
        # 各グループの総和を保持するリストを初期化
        group_sums = [0] * D

        # グループを表す2次元リストを初期化
        groups = [[] for _ in range(D)]
        groups_id = [[] for _ in range(D)]

        # 重みを降順にソート
        sorted_weights = sorted([[w, i] for i, w in enumerate(W)], reverse=True)

        for w, i in sorted_weights:
            # 現時点で最小の合計重みを持つグループを見つける
            min_group_idx = group_sums.index(min(group_sums))

            # そのグループに重みを追加
            groups[min_group_idx].append(w)
            groups_id[min_group_idx].append(i)

            # グループの合計重みを更新
            group_sums[min_group_idx] += w

        return groups, groups_id

    groups, groups_id = greedy_partition(EW, D)
    ans = [0] * N
    for d, IDs in enumerate(groups_id):
        for i in IDs:
            ans[i] = d

    print(*ans, flush=True)

    if IS_LOCAL:
        import numpy as np
        def calc_score(result_ids):
            sums = []
            for i, ids in enumerate(result_ids):
                group = [W[id] for id in ids]
                sums.append(np.sum(group))
            return round(np.std(sums) * 100)

        def estimate_score(result):
            sums = []
            for i, ws in enumerate(result):
                group = [w for w in ws]
                sums.append(np.sum(group))
            return round(np.std(sums) * 100)

        res = calc_score(groups_id)
        est = estimate_score(groups)
        return res, est

    else:
        return


def main():
    if IS_LOCAL:
        in_files = sorted(list(Path("./in/").glob("*.txt")))

        Inputs = []
        for p in in_files:
            with open(p, mode="r") as f:
                N, D, Q = map(int, f.readline().split())
                W = list(map(int, f.readline().split()))
                Inputs.append([N, D, Q, W])

        Results = []
        for i, (N, D, Q, W) in enumerate(Inputs):
            if i <= 100:
                f = f"{str(i).zfill(4)}.png"

                score_sum = 0
                r = min(int(50*N/Q), N//2)
                score, est = solve_randommatch(N, D, Q, W, root=r, f=f)
                score_sum += score

                Results.append([N, D, Q, score, est])

        import pandas as pd
        df = pd.DataFrame(Results, columns=["N", "D", "Q", "score", "est"])
        df.to_csv("./res_score_est_sqrt.csv", index=False)

    else:
        N, D, Q = NMI()
        solve_randommatch(N, D, Q, W=None, root=N//2, f=None)



if __name__ == "__main__":
    main()
