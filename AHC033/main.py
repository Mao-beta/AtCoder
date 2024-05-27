import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


def bigonly(N, A):
    # 大アームで小さいほうから全部なんとかする
    # 他は全部爆破
    ans = [[] for _ in range(5)]
    for i in range(1, 5):
        ans[i].append("B")

    A = [deque(a) for a in A]

    containers = []
    for Ai in A:
        a = Ai.popleft()
        containers.append(a)

    INF = 100

    def yoko_move(i, j, i2, j2):
        # 2点間の移動をあらわす文字列 横から
        res = []
        if j < j2:
            for k in range(abs(j2-j)):
                res.append("R")
        else:
            for k in range(abs(j2-j)):
                res.append("L")

        if i < i2:
            for k in range(abs(i2-i)):
                res.append("D")
        else:
            for k in range(abs(i2-i)):
                res.append("U")

        return res

    def tate_move(i, j, i2, j2):
        # 2点間の移動をあらわす文字列 縦から
        res = []

        if i < i2:
            for k in range(abs(i2 - i)):
                res.append("D")
        else:
            for k in range(abs(i2 - i)):
                res.append("U")

        if j < j2:
            for k in range(abs(j2 - j)):
                res.append("R")
        else:
            for k in range(abs(j2 - j)):
                res.append("L")

        return res


    ni, nj = 0, 0
    while sum(containers) < 5*INF:
        target = min(containers)
        ti = containers.index(target)
        tj = 0
        gi = target // N
        gj = N-1
        ans[0] += tate_move(ni, nj, ti, tj)
        ni, nj = ti, tj
        ans[0].append("P")
        ans[0] += yoko_move(ni, nj, gi, gj)
        ni, nj = gi, gj
        ans[0].append("Q")

        if A[ti]:
            a = A[ti].popleft()
            containers[ti] = a
        else:
            containers[ti] = INF

    for row in ans:
        print("".join(row))


def big_and_short4(N, A):
    # 大アーム(上3列)と小4アーム(下2列)で小さいほうからなんとかする
    # 他は全部爆破
    ans = [[] for _ in range(5)]
    for i in range(1, 4):
        ans[i].append("B")

    A = [deque(a) for a in A]

    containers = []
    for Ai in A:
        a = Ai.popleft()
        containers.append(a)

    INF = 100

    def yoko_move(i, j, i2, j2):
        # 2点間の移動をあらわす文字列 横から
        res = []
        if j < j2:
            for k in range(abs(j2-j)):
                res.append("R")
        else:
            for k in range(abs(j2-j)):
                res.append("L")

        if i < i2:
            for k in range(abs(i2-i)):
                res.append("D")
        else:
            for k in range(abs(i2-i)):
                res.append("U")

        return res

    def tate_move(i, j, i2, j2):
        # 2点間の移動をあらわす文字列 縦から
        res = []

        if i < i2:
            for k in range(abs(i2 - i)):
                res.append("D")
        else:
            for k in range(abs(i2 - i)):
                res.append("U")

        if j < j2:
            for k in range(abs(j2 - j)):
                res.append("R")
        else:
            for k in range(abs(j2 - j)):
                res.append("L")

        return res


    ni, nj = 0, 0
    while sum(containers[:3]) < 3*INF:
        target = min(containers[:3])
        ti = containers.index(target)
        tj = 0
        gi = target // N
        gj = N-1
        ans[0] += tate_move(ni, nj, ti, tj)
        ni, nj = ti, tj
        ans[0].append("P")
        ans[0] += yoko_move(ni, nj, gi, gj)
        ni, nj = gi, gj
        ans[0].append("Q")

        if A[ti]:
            a = A[ti].popleft()
            containers[ti] = a
        else:
            containers[ti] = INF


    ni, nj = 4, 0
    while sum(containers[3:]) < 2 * INF:
        target = min(containers[3:])
        ti = containers.index(target)
        tj = 0
        gi = target // N
        gj = N - 1
        ans[4] += tate_move(ni, nj, ti, tj)
        ni, nj = ti, tj
        ans[4].append("P")
        ans[4] += yoko_move(ni, nj, gi, gj)
        ni, nj = gi, gj
        ans[4].append("Q")

        if A[ti]:
            a = A[ti].popleft()
            containers[ti] = a
        else:
            containers[ti] = INF

    ans[4].append("B")


    # 微調整
    DIJ = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1], "P": [0, 0], "Q": [0, 0]}
    bi, bj = 0, 0
    si, sj = 4, 0
    for i in range(10000):
        if i < len(ans[0]):
            b = ans[0][i]
            di, dj = DIJ[b]
            if sj == 4 and bj + dj == 4:
                ans[0].insert(i, ".")
            else:
                bi += di
                bj += dj
        else:
            break

        if i < len(ans[4]):
            b = ans[4][i]
            if b == "B":
                si, sj = 4, 0
                continue
            di, dj = DIJ[b]
            if bj == 4 and sj + dj == 4:
                ans[4].insert(i, ".")
            else:
                si += di
                sj += dj


    for row in ans:
        print("".join(row))


def display(N, A):
    # 最初に左4列使って20個並べる
    # 小クレーン爆破して大だけで運ぶ

    ans = [[] for _ in range(N)]

    ans[0].append("PRRRQLLLPRRQLLPRQ")
    for i in range(1, N):
        ans[i].append("PRRRQLLLPRRQLLPRQB")

    IJ = [[-1, -1] for _ in range(25)]
    A = [deque(a) for a in A]
    G = [[-1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            a = A[i].popleft()
            G[i][N-2-j] = a
            IJ[a] = [i, N-2-j]
        IJ[A[i][0]] = [i, -1]

    # print(*IJ)

    def yoko_move(i, j, i2, j2):
        # 2点間の移動をあらわす文字列 横から
        res = []
        if j < j2:
            for k in range(abs(j2-j)):
                res.append("R")
        else:
            for k in range(abs(j2-j)):
                res.append("L")

        if i < i2:
            for k in range(abs(i2-i)):
                res.append("D")
        else:
            for k in range(abs(i2-i)):
                res.append("U")

        return res

    def tate_move(i, j, i2, j2):
        # 2点間の移動をあらわす文字列 縦から
        res = []

        if i < i2:
            for k in range(abs(i2 - i)):
                res.append("D")
        else:
            for k in range(abs(i2 - i)):
                res.append("U")

        if j < j2:
            for k in range(abs(j2 - j)):
                res.append("R")
        else:
            for k in range(abs(j2 - j)):
                res.append("L")

        return res

    targets = {0, 5, 10, 15, 20}

    ni, nj = 0, 1
    # 1ターンごとの処理
    while targets:
        ok = False
        for j in range(N):
            for i in range(N):
                if G[i][j] in targets:
                    a = G[i][j]
                    ok = True
                    ans[0] += tate_move(ni, nj, i, j)
                    ans[0].append("P")
                    ti, tj = a // N, N-1
                    ans[0] += tate_move(i, j, ti, tj)
                    ans[0].append("Q")
                    ni, nj = ti, tj
                    targets.discard(a)
                    if a % N < 4:
                        targets.add(a+1)
                    G[i][j] = -1
                    if A[i] and j == 0:
                        G[i][j] = A[i].popleft()
                if ok:
                    break
            if ok:
                break

        if not ok:
            for i in range(N):
                if A[i] and G[i][0] >= 0:
                    flg = False
                    a = G[i][0]
                    for h in range(N):
                        for w in range(1, N-1):
                            if G[h][w] >= 0:
                                continue
                            flg = True
                            ans[0] += tate_move(ni, nj, i, 0)
                            ans[0].append("P")
                            ans[0] += tate_move(i, 0, h, w)
                            ans[0].append("Q")
                            ni, nj = h, w
                            G[h][w] = a
                            G[i][0] = A[i].popleft()
                            break
                        if flg:
                            break


    for row in ans:
        print("".join(row))



class MoveString:
    def __init__(self):
        pass

    def left(self, i):
        return "L" * i

    def right(self, i):
        return "R" * i

    def up(self, i):
        return "U" * i

    def down(self, i):
        return "D" * i

    def yoko(self, x, y):
        if y > x:
            return self.right(y-x)
        else:
            return self.left(x-y)

    def tate(self, x, y):
        if y > x:
            return self.down(y-x)
        else:
            return self.up(x-y)

    def pick(self):
        return "P"

    def put(self):
        return "Q"

    def move(self, si, sj, ti, tj, yoko_first=True):
        res = ""
        if yoko_first:
            res += self.yoko(sj, tj)
            res += self.tate(si, ti)
        else:
            res += self.tate(si, ti)
            res += self.yoko(sj, tj)
        return res

    def bring(self, si, sj, ti, tj, yoko_first=True):
        res = self.pick() + self.move(si, sj, ti, tj, yoko_first) + self.put()
        return res


class Game:
    def __init__(self, A):
        self.N = 5
        self.A = [deque(Ai) for Ai in A]
        self.IJ = [[-1, -1] for _ in range(25)]
        self.B = [[-1]*5 for _ in range(5)]
        self.ans = [[] for _ in range(5)]
        self.arms = [[i, 0] for i in range(5)]

    def search(self, a):
        i, j = self.IJ[a]
        return i, j

    def enter(self, i):
        # i行目の在庫を0列目に置く
        assert self.B[i][0] == -1
        assert self.A[i]
        a = self.A[i].popleft()
        self.B[i][0] = a
        self.IJ[a] = [i, 0]

    def display(self):
        # 左4列埋めて下4つのアームは爆破
        self.ans[0].append("PRRRQLLLPRRQLLPRQ")
        for i in range(1, N):
            self.ans[i].append("PRRRQLLLPRRQLLPRQB")

        for i in range(N):
            for j in range(N - 1):
                a = self.A[i].popleft()
                self.B[i][N - 2 - j] = a
                self.IJ[a] = [i, N - 2 - j]
            self.IJ[A[i][0]] = [i, -1]
            self.arms[i] = [-1, -1]

        self.arms[0] = [0, 1]




    def display_and_greedy(self):
        M = MoveString()

        self.display()
        self.debug()

        targets = {0, 5, 10, 15, 20}

        # 1ターンごとの処理
        while targets:
            # targetsの中から行けるものを探す

            pass
            # ok = False
            # for j in range(N):
            #     for i in range(N):
            #         if self.B[i][j] in targets:
            #             a = self.B[i][j]
            #             ok = True
            #             self.ans[0].append(M.bring(ni, nj, i, j))
            #             ti, tj = a // N, N - 1
            #             self.ans[0] += tate_move(i, j, ti, tj)
            #             self.ans[0].append("Q")
            #             ni, nj = ti, tj
            #             targets.discard(a)
            #             if a % N < 4:
            #                 targets.add(a + 1)
            #             self.B[i][j] = -1
            #             if self.A[i] and j == 0:
            #                 self.B[i][j] = self.A[i].popleft()
            #         if ok:
            #             break
            #     if ok:
            #         break
            #
            # if not ok:
            #     for i in range(N):
            #         if self.A[i] and G[i][0] >= 0:
            #             flg = False
            #             a = G[i][0]
            #             for h in range(N):
            #                 for w in range(1, N - 1):
            #                     if G[h][w] >= 0:
            #                         continue
            #                     flg = True
            #                     ans[0] += tate_move(ni, nj, i, 0)
            #                     ans[0].append("P")
            #                     ans[0] += tate_move(i, 0, h, w)
            #                     ans[0].append("Q")
            #                     ni, nj = h, w
            #                     G[h][w] = a
            #                     G[i][0] = A[i].popleft()
            #                     break
            #                 if flg:
            #                     break

    def debug(self):
        print("board:", *self.B, sep="\n", file=sys.stderr)
        print("arms:", self.arms, file=sys.stderr)


def main(N, A):
    G = Game(A)
    G.display_and_greedy()


if __name__ == "__main__":
    N = NI()
    A = EI(N)
    main(N, A)
