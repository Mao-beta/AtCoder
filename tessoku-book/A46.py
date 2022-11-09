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

import time
from random import randint, uniform


class TSP:
    """
    巡回セールスマンのHeuristic
    1-index
    """
    def __init__(self, N, XY):
        self.loop = 0
        self.START_TIME = time.time()
        self.LIMIT_TIME = 0.86

        self.N = N
        self.XY = XY
        self.D = self.calc_D()

        # indexは0-Nまで
        self.ans = list(range(1, N+1)) + [1]
        self.score = self.get_score()

        self.best_ans = self.ans[:]
        self.best_score = self.score


    def is_time_over(self):
        return time.time() - self.START_TIME > self.LIMIT_TIME


    def yamanobori(self):
        while not self.is_time_over():
            l, r = self.pick_lr()
            self.rev_ans(l, r)
            new_score = self.get_score()

            if self.score > new_score:
                self.score = new_score
            else:
                self.rev_ans(l, r)

            self.loop += 1

            # print(self)


    def annealing(self):
        while not self.is_time_over():
            l, r = self.pick_lr()
            self.rev_ans(l, r)
            new_score = self.get_score()

            ratio = (time.time() - self.START_TIME) / self.LIMIT_TIME
            T = 30 - 28 * ratio
            proba = math.exp(min(0.0, (self.score - new_score) / T))

            if random.uniform(0, 1) < proba:
                self.score = new_score
            else:
                self.rev_ans(l, r)

            self.loop += 1
            # print(self)


    def annealing_diff(self):
        while not self.is_time_over():
            l, r = self.pick_lr()

            now_c = self.D[self.ans[l-1]][self.ans[l]] + self.D[self.ans[r-1]][self.ans[r]]
            new_c = self.D[self.ans[l-1]][self.ans[r-1]] + self.D[self.ans[l]][self.ans[r]]

            ratio = (time.time() - self.START_TIME) / self.LIMIT_TIME
            T = 30 - 28 * ratio
            proba = math.exp(min(0.0, (now_c - new_c) / T))

            if random.uniform(0, 1) < proba:
                self.rev_ans(l, r)
                self.score = self.get_score()

                if self.score < self.best_score:
                    self.best_score = self.score
                    self.best_ans = self.ans[:]

            else:
                pass

            self.loop += 1
            # print(self)


    def pick_lr(self):
        l = randint(1, self.N-1)
        r = randint(l+1, self.N)
        return l, r


    def rev_ans(self, l, r):
        self.ans[l:r] = self.ans[l:r][::-1]


    def get_score(self):
        res = 0
        for i in range(self.N):
            res += self.D[self.ans[i]][self.ans[i+1]]
        return res


    def calc_dist(self, i, j):
        xi, yi = self.XY[i]
        xj, yj = self.XY[j]
        return ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5


    def calc_D(self):
        INF = 10**10
        D = [[INF]*(self.N+1) for _ in range(self.N+1)]
        for i in range(1, self.N+1):
            for j in range(1, self.N+1):
                D[i][j] = self.calc_dist(i, j)
        return D


    def __str__(self):
        return f"now score: {self.get_score()}" #\nnow ans: {self.ans}"


def main():
    import time
    from random import randint, uniform

    N = NI()
    XY = [[0, 0]] + [NLI() for _ in range(N)]

    tsp = TSP(N, XY)
    # print(tsp)

    tsp.annealing_diff()

    print(*tsp.best_ans, sep="\n")
    # print(tsp.loop)


def _main():
    import time
    from random import randint, uniform

    N = NI()
    XY = [NLI() for _ in range(N)]

    start_time = time.time()

    INF = 10**10

    D2 = [[INF]*N for _ in range(N)]
    for i in range(N):
        xi, yi = XY[i]
        for j in range(N):
            xj, yj = XY[j]
            D2[i][j] = ((xi-xj) ** 2 + (yi-yj) ** 2) ** 0.5

    now = 0
    res = set(range(1, N))
    ans = [now+1]

    while res:
        D2s = []
        for r in res:
            D2s.append((D2[now][r], r))
        D2s.sort()
        goto = D2s[0][1]
        res.discard(goto)
        now = goto
        ans.append(now+1)

    ans.append(1)

    ans = [1] + list(range(2, N+1)) + [1]

    assert len(ans) == N+1

    def gap(i):
        # ans[i]からans[i+1]までのD2を取得
        assert 0 <= i <= N
        return D2[ans[i]-1][ans[i+1]-1]

    # print(len(ans))
    # print(ans)

    # 2-opt
    # ans[x] -> ans[x+1], ans[y] -> ans[y+1] の2経路を
    # ans[x] -> ans[y+1], ans[y] -> ans[x+1] に組み替え
    # その間は逆順にする
    def two_opt(ans):
        x = randint(0, N-1)
        y = randint(0, N-1)
        if x >= y: return

        # print(x, y)

        before = gap(x) + gap(y)
        ans[x+1: y+1] = reversed(ans[x+1: y+1])
        after = gap(x) + gap(y)

        # diff < 0 のとき悪化
        diff = before - after


        now = time.time() - start_time
        ratio = now / 0.85
        start_temp = 1
        end_temp = 0.0001
        temp = start_temp + (end_temp - start_temp) * ratio
        try:
            proba = math.exp(diff / temp)
        except:
            proba = 0

        # if diff < 0:
        #     print(proba, ratio)

        if diff > 0 or proba > uniform(0, 1):
            return
        else:
            ans[x + 1: y + 1] = reversed(ans[x + 1: y + 1])
            return


    while time.time() - start_time < 0.85:
        two_opt(ans)
        # print(ans)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
