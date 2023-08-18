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


IS_DEBUG = False
try:
    import matplotlib
    IS_DEBUG = True
except:
    pass

# IS_DEBUG = False




def _main():
    L, N, S = NMI()
    YX = EI(N)
    A = None
    F = None

    if IS_DEBUG:
        A = [NI() for _ in range(N)]
        F = [NI() for _ in range(10000)]
    
    G = [[N*10//L * y]*L for y in range(L)]
    for i, (y, x) in enumerate(YX):
        G[y][x] = i * 10



    for row in G:
        print(*row, flush=True)

    # i番目のワームホールでの温度の推定値
    V = [0] * N

    mi = 0

    for i in range(N):
        vs = []
        K = max(1, min(10000//N, int(S**2/4)*2))
        for _ in range(K):
            print(i, 0, 0, flush=True)
            if IS_DEBUG:
                ay, ax = YX[A[i]]
                v = max(0, min(1000, G[ay][ax] + F[mi]))
                mi += 1
            else:
                v = NI()

            # print("#", i, v, ay, ax, mi, F[mi])

            if v == -1:
                raise ValueError

            vs.append(v)

        print("#", vs)
        V[i] = sum(vs) / len(vs)

    ans = [0] * N

    for i in range(N):
        tmp_gap = 100000
        tmp_ai = 0
        v = V[i]
        for ai, (y, x) in enumerate(YX):
            gap = abs(G[y][x] - v)
            if gap < tmp_gap:
                tmp_gap = gap
                tmp_ai = ai

        ans[i] = tmp_ai

    print("#", V)
    print(-1, -1, -1)
    print(*ans, sep="\n", flush=True)


def erf(z):
    """Approximate the error function."""
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911

    sign = 1 if z >= 0 else -1
    z = abs(z)

    t = 1.0 / (1.0 + p * z)
    y = (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t

    return sign * (1 - y * math.exp(-z * z))

def normal_cdf(x, m, s):
    """Compute the CDF for a normal distribution."""
    return 0.5 * (1 + erf((x - m) / (s * math.sqrt(2))))


from typing import List

class Judge:
    def __init__(self, L, A, F, YX):
        self.is_debug = IS_DEBUG
        self.L = L
        self.A = A
        self.F = F
        self.outputs = []
        self.m_cnt = 0
        self.temperature = None
        self.YX = YX

    def set_temperature(self, P: List[List[int]]):
        self.temperature = P
        for row in P:
            print(*row, flush=True)
            if self.is_debug:
                self.outputs.append(" ".join(map(str, row)))

    def measure(self, i: int, y: int, x: int) -> int:
        print(i, y, x, flush=True)
        if self.is_debug:
            self.outputs.append(f"{i} {y} {x}")
            a = self.A[i]
            ay, ax = self.YX[a]
            p = self.temperature[(ay+y)%self.L][(ax+x)%self.L]
            m = p + self.F[self.m_cnt]
            m = max(0, min(1000, m))

        else:
            m = NI()

        self.m_cnt += 1
        return m

    def answer(self, E: List[int]):
        print(-1, -1, -1, flush=True)
        print(*E, sep="\n", flush=True)
        if self.is_debug:
            self.outputs.append("-1 -1 -1")
            for e in E:
                self.outputs.append(e)

    def __repr__(self):
        return f"A={self.A}"


class Solver:
    def __init__(self, L, N, S, YX, A, F):
        self.L = L
        self.N = N
        self.S = S
        self.A = A
        self.YX = YX
        self.judge = Judge(L, A, F, YX)


    def make_temperature(self):
        self.P = [[0] * self.L for _ in range(self.L)]
        # for i, (y, x) in enumerate(self.YX):
        #     self.P[y][x] += i * 200
        cy, cx = self.L / 2, self.L / 2
        for y in range(self.L):
            for x in range(self.L):
                dy, dx = y-cy, x-cx
                l = int(math.sqrt(dx**2 + dy**2))
                p = 900 - 8000*l / (7*self.L)
                if y % 3 and x % 3:
                    p -= 100
                self.P[y][x] = max(0, min(1000, round(self.P[y][x] + p)))


    def make_temperature_highS(self):
        self.P = [[self.N * 10 // self.L * y] * self.L for y in range(self.L)]
        for i, (y, x) in enumerate(self.YX):
            self.P[y][x] = i * 10
        # for i, (y, x) in enumerate(self.YX):
        #     self.P[y][x] = max(0, min(1000, round(1000 * i / self.N)))


    def calc_YX_9cells(self):
        self.yx_9cells = []
        DY = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        DX = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        for i, (y, x) in enumerate(self.YX):
            tmp = []
            k = 1
            for dy, dx in zip(DY, DX):
                ny, nx = (y+dy*k) % self.L, (x+dx*k) % self.L
                tmp.append(self.P[ny][nx])
            self.yx_9cells.append(tmp[:])


    def measure_9cells(self, i):
        DY = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        DX = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
        res = []
        k = 1
        for dy, dx in zip(DY, DX):
            m = self.judge.measure(i, dy*k, dx*k)
            res.append(m)

        if IS_DEBUG:
            print("#", res)
        return res


    def rmse(self, D1, D2):
        res = 0
        for d1, d2 in zip(D1, D2):
            res += (d2-d1) ** 2
        res = math.sqrt(res)
        return res

    def mae(self, D1, D2):
        res = 0
        for d1, d2 in zip(D1, D2):
            res += abs(d2-d1)
        return res


    def prob(self, D1, D2):
        res = 1
        for d1, d2 in zip(D1, D2):
            p = 1 - normal_cdf(d1, abs(d2-d1) + d1, self.S)
            res *= p
        return res


    def maxgap(self, D1, D2):
        res = 0
        for d1, d2 in zip(D1, D2):
            res = max(res, (d2-d1)**4)
        return res


    def solve(self):
        self.make_temperature_balance()
        self.judge.set_temperature(self.P)
        self.calc_YX_9cells()

        D = [[0.0]*9 for _ in range(self.N)]
        if self.S <= 1**2:
            K = 1
        elif self.S <= 2**2:
            K = 1
        elif self.S <= 3**2:
            K = 3
        else:
            K = 11

        for i in range(self.N):
            for k in range(K):
                res = self.measure_9cells(i)
                for j, r in enumerate(res):
                    D[i][j] += r
            D[i] = [d/K for d in D[i]]

        ans = [0] * self.N

        for i in range(self.N):
            tmp_gap = 10**20
            tmp_ai = 0
            tmp_p = 0
            for ai, (y, x) in enumerate(self.YX):
                gap = self.rmse(self.yx_9cells[ai], D[i])
                p = self.prob(self.yx_9cells[ai], D[i])
                if p < 0.001:
                    continue
                if gap < tmp_gap:
                    tmp_gap = gap
                    tmp_ai = ai

            ans[i] = tmp_ai
            if IS_DEBUG:
                print("#", ans[i], i, self.A[i], self.yx_9cells[ans[i]], D[i], self.yx_9cells[self.A[i]])

        self.judge.answer(ans)


    def solve_highS(self):
        self.make_temperature_highS()
        self.judge.set_temperature(self.P)
        self.calc_YX_9cells()

        K = 100
        D = [[0.0]*K for _ in range(self.N)]

        for i in range(self.N):
            for k in range(K):
                res = self.judge.measure(i, 0, 0)
                D[i][k] += res

        print("#", D)

        ans = [0] * self.N

        for i in range(self.N):
            tmp_gap = 10**20
            tmp_ai = 0
            for ai, (y, x) in enumerate(self.YX):
                DA = [self.P[y][x] for k in range(K)]

                gap = self.rmse(DA, D[i])
                if gap < tmp_gap:
                    tmp_gap = gap
                    tmp_ai = ai

            ans[i] = tmp_ai
            if IS_DEBUG:
                y, x = self.YX[ans[i]]
                ay, ax = self.YX[self.A[i]]
                print("#", ans[i], i, self.A[i], self.P[y][x], sum(D[i])/K, self.P[ay][ax])

        self.judge.answer(ans)


    def solve_random(self):
        self.P = [[0] * self.L for _ in range(self.L)]
        self.judge.set_temperature(self.P)
        ans = [0] * self.N
        self.judge.answer(ans)


    def make_temperature_balance(self):
        self.P = [[0] * self.L for _ in range(self.L)]
        gap = 1000 // (self.N + 1)

        if self.S == 1**2:
            gap = 5
        elif self.S == 2**2:
            gap = 5
        # T = [gap * (i+1) for i in range(self.N)]

        cy, cx = self.L / 2, self.L / 2
        order = []
        for ai, (ay, ax) in enumerate(self.YX):
            l = (cy - ay) ** 2 + (cx - ax) ** 2
            order.append([l, ai])
        order.sort()

        T = [[ai, gap * (i + 1)] for i, (l, ai) in enumerate(order)]
        T.sort()
        T = [p for ai, p in T]

        for y in range(self.L):
            for x in range(self.L):
                C = []
                p = None
                for ai, (ay, ax) in enumerate(self.YX):
                    dy, dx = abs(y - ay), abs(x - ax)
                    d = min(self.L - dy, dy) + min(self.L - dx, dx)
                    if d == 0:
                        p = T[ai]
                        break
                    else:
                        C.append((1 / (d - 0.7)) ** 2.5)

                if p is None:
                    p = 0
                    for ai, c in enumerate(C):
                        p += T[ai] * c

                    self.P[y][x] = int(p / sum(C))

                else:
                    self.P[y][x] = p


    def solve_temperature_balance(self):
        self.make_temperature_balance()
        self.judge.set_temperature(self.P)

        K = 10000 // self.N
        if self.S == 1:
            K = 5

        M = [0] * self.N
        for ai in range(self.N):
            for k in range(K):
                m = self.judge.measure(ai, 0, 0)
                M[ai] += m
            M[ai] //= K

        ans = [0] * self.N

        for i in range(self.N):
            tmp_gap = 100000
            tmp_ai = 0
            m = M[i]
            for ai, (y, x) in enumerate(self.YX):
                gap = abs(self.P[y][x] - m)
                if gap < tmp_gap:
                    tmp_gap = gap
                    tmp_ai = ai

            ans[i] = tmp_ai

        print("#", M)
        print(-1, -1, -1)
        print(*ans, sep="\n", flush=True)


    def __repr__(self):
        return f"L={self.L}, N={self.N}, S={self.S}, {self.judge}\n# YX={self.YX}"



# S1のときは5刻み、1回？

def take_input(path=None):
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            L, N, S = map(int, inputs[0].split())
            YX = []
            for i in range(N):
                yx = list(map(int, inputs[1+i].split()))
                YX.append(yx)
            A = []
            F = []
            for i in range(N):
                A.append(int(inputs[1+N+i].split()[0]))
            for i in range(10000):
                F.append(int(inputs[1+N+N+i].split()[0]))

    else:
        L, N, S = NMI()
        YX = [NLI() for _ in range(N)]
        A = None
        F = None

    return L, N, S, YX, A, F



def main(L, N, S, YX, A, F, outpath):
    solver = Solver(L, N, S, YX, A, F)
    print("#", solver)
    # solver.solve_temperature_balance()
    if S <= 15**2 or N >= 81:
        solver.solve()
    else:
        # N >= 94だと結局1点
        solver.solve_random()


# IS_DEBUG = False
if __name__ == "__main__":
    if IS_DEBUG:
        k = 80
        for i in range(k, k+1):
            path = f"./in/{str(i).zfill(4)}.txt"
            inputs = take_input(path)
            outpath = f"./out/{str(i).zfill(4)}.txt"
            ans = main(*inputs, outpath)
    else:
        ans = main(*take_input(), None)
