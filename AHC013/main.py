import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
import pprint

try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False


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


# URDL
DH = [-1, 0, 1, 0]
DW = [0, 1, 0, -1]


def on_board(h, w, N):
    return 0 <= h < N and 0 <= w < N


def search(h, w, d, C):
    N = len(C)
    dh, dw = DH[d], DW[d]
    while True:
        h += dh
        w += dw
        if not on_board(h, w, N):
            return N, N, 0
        if C[h][w] != 0:
            return h, w, C[h][w]

def paint(sh, sw, th, tw, C):
    if sh == th:
        if sw > tw:
            sw, tw = tw, sw
        for w in range(sw+1, tw):
            C[sh][w] = -1

    elif sw == tw:
        if sh > th:
            sh, th = th, sh
        for h in range(sh+1, th):
            C[h][sw] = -1


def output(M_ans, C_ans):
    print(len(M_ans))
    for row in M_ans:
        print(*row)
    print(len(C_ans))
    for row in C_ans:
        print(*row)


def output_file(M_ans, C_ans, outpath):
    with open(outpath, "w") as f:
        f.write(str(len(M_ans)) + "\n")
        for row in M_ans:
            f.write(" ".join(map(str, row)) + "\n")

        f.write(str(len(C_ans)) + "\n")
        for row in C_ans:
            f.write(" ".join(map(str, row)) + "\n")


class Cluster:
    def __init__(self):
        self.Vs = set()
        self.pipes = []

    def add(self, V, newV):
        self.Vs.add(newV)
        self.pipes.append(Pipe(*V, *newV))


class CPU:
    def __init__(self, h, w, k, idx):
        self.h = h
        self.w = w
        self.k = k
        self.idx = idx
        self.connected = 0 # 4bit

    def move(self, d):
        self.h += DH[d]
        self.w += DW[d]

    def __str__(self):
        return f"C{str(self.idx).zfill(3)} h: {self.h}, w: {self.w}, k: {self.k}"

    def __repr__(self):
        return f"C{str(self.idx).zfill(3)}"


class Pipe:
    NN = 50
    def __init__(self, ph, pw, qh, qw):
        if ph == qh:
            if pw > qw: pw, qw = qw, pw
            pd, qd = 1, 3
            self.is_horizontal = True
        else:
            if ph > qh: ph, qh = qh, ph
            pd, qd = 2, 0
            self.is_horizontal = False

        self.P = (ph, pw, pd)
        self.Q = (qh, qw, qd)
        self.idx = self.P[0] * self.NN**3 + self.P[1] * self.NN**2 + self.Q[0] * self.NN + self.Q[1]

    def __str__(self):
        return f"Pipe ({self.P[0]}, {self.P[1]}) - ({self.Q[0]}, {self.Q[1]})"

    def __repr__(self):
        return "----" if self.P[0] == self.Q[0] else "||||"

    def __eq__(self, other):
        if not isinstance(other, Pipe):
            return False
        return self.idx == other.idx

    def __hash__(self):
        return hash(self.idx)


class AllPipes:
    def __init__(self, N):
        self.N = N
        self.pipes = set()
        self.ison = [[0]*(N**2) for _ in range(N**2)]

    def pipe_ids(self, pipe: Pipe):
        px, py = pipe.P
        qx, qy = pipe.Q
        pi = px * self.N + py
        qi = qx * self.N + qy
        return pi, qi

    def id2hw(self, pipe_id):
        return divmod(pipe_id, self.N)

    def is_on(self, pipe: Pipe):
        pi, qi = self.pipe_ids(pipe)
        return self.ison[pi][qi]

    def add_pipe(self, pipe: Pipe):
        pi, qi = self.pipe_ids(pipe)
        self.ison[pi][qi] = 1
        self.ison[qi][pi] = 1
        self.pipes.add(pipe)

    def __str__(self):
        return "\n".join(map(str, self.pipes))


class Board:
    """
    盤面管理クラス
    座標を見るとどのCPUがいるか、またはどのPipeかがわかる（idxが見える）
    """
    DH = [-1, 0, 1, 0]
    DW = [0, 1, 0, -1]

    def __init__(self, C):
        self.N = len(C)
        self.C = [["  "] * self.N for _ in range(self.N)]
        self.Pipes = AllPipes(self.N)
        idxs = [i*100 for i in range(6)]
        for h in range(self.N):
            for w in range(self.N):
                if C[h][w] != 0:
                    cpu = CPU(h, w, C[h][w], idxs[C[h][w]])
                    self.C[h][w] = cpu
                    idxs[C[h][w]] += 1


    # 判定系
    def on_board(self, h, w):
        return 0 <= h < self.N and 0 <= w < self.N

    def color(self, h, w):
        if not self.on_board(h, w):
            return -1

        if not isinstance(self.C[h][w], CPU):
            return 0

        return self.C[h][w].k

    def movable(self, h, w):
        if not self.on_board(h, w):
            return False

        if not isinstance(self.C[h][w], CPU):
            return True
        else:
            return False


    def search_cpu(self, h, w, d):
        dh, dw = self.DH[d], self.DW[d]
        while True:
            h += dh
            w += dw
            if not self.on_board(h, w):
                return self.N, self.N, 0
            obj = self.C[h][w]
            if isinstance(obj, Pipe):
                return self.N, self.N, 0

            if isinstance(obj, CPU):
                return h, w, obj.k


    # 操作系
    def move_cpu(self, sh, sw, th, tw):
        if not self.movable(th, tw):
            return


    def search_and_connect(self, sh, sw, d):
        cpu_s = self.C[sh][sw]
        if not isinstance(cpu_s, CPU):
            return

        # 方向dを探し、同じ色ならつなぐ
        th, tw, tk = self.search_cpu(sh, sw, d)
        if cpu_s.k == tk:
            self.connect_cpus(sh, sw, th, tw)


    def connect_cpus(self, sh, sw, th, tw):
        # CPUがある前提
        pipe = Pipe(sh, sw, th, tw)
        self.add_pipe(pipe)



    def add_pipe(self, pipe:Pipe):
        self.Pipes.add_pipe(pipe)
        self.lay_pipe(pipe)


    def lay_pipe(self, pipe: Pipe):
        sh, sw, sd = pipe.P
        th, tw, td = pipe.Q

        if sh == th:
            if sw > tw:
                sw, tw = tw, sw
            for w in range(sw + 1, tw):
                self.C[sh][w] = pipe

        elif sw == tw:
            if sh > th:
                sh, th = th, sh
            for h in range(sh + 1, th):
                self.C[h][sw] = pipe


    # 表示系
    def __str__(self):
        res = "Board\n"
        res += pprint.pformat(self.C, width=1000)
        return res


def main(N, K, C):
    M_ans = []
    C_ans = []

    # CPUを初期化
    board = Board(C)


    # つなげるだけPipeをつなぐ
    # for target in range(1, K+1):
    #     for h in range(N-1, -1, -1):
    #         for w in range(N-1, -1, -1):
    #             c = C[h][w]
    #             if c != target: continue
    #             flag = True
    #             for d in [1, 2]:
    #                 th, tw, tc = search(h, w, d, C)
    #                 if c == tc:
    #                     C_ans.append([h, w, th, tw])
    #                     board.add_pipe(Pipe(h, w, th, tw))
    #                     flag = False
    #
    #             if flag:
    #                 # 左下か左上が同じ色なら左にずらす
    #                 if is_this_color(h+1, w-1, c, N, C) or is_this_color(h-1, w-1, c, N, C):
    #                     if movable(h, w-1, N, C):
    #                         C[h][w], C[h][w-1] = C[h][w-1], C[h][w]
    #                         M_ans.append([h, w, h, w-1])
    #
    #                 # そうでなく右上が同じなら上にずらす
    #                 elif is_this_color(h-1, w+1, c, N, C):
    #                     if movable(h-1, w, N, C):
    #                         C[h][w], C[h-1][w] = C[h-1][w], C[h][w]
    #                         M_ans.append([h, w, h-1, w])

    for target in range(1, K+1):
        for h in range(N):
            for w in range(N):
                for d in [1, 2]:
                    board.search_and_connect(h, w, d)

    print(board)

    # あるCPUに注目し、隣接マスに同じ色のPipeがあればのっかる
    # つまり、盤面を見たらそこがどのCPUとどのCPUのPipe上か高速に知れたらよい


    return M_ans, C_ans


def movable(h, w, N, C):
    return on_board(h, w, N) and C[h][w] == 0


def is_this_color(h, w, c, N, C):
    return on_board(h, w, N) and C[h][w] == c


def _main(N, K, C):
    M_ans = []
    C_ans = []

    for target in range(1, K+1):
        for h in range(N-1, -1, -1):
            for w in range(N-1, -1, -1):
                c = C[h][w]
                if c != target: continue
                flag = True
                for d in [1, 2]:
                    th, tw, tc = search(h, w, d, C)
                    if c == tc:
                        C_ans.append([h, w, th, tw])
                        paint(h, w, th, tw, C)
                        flag = False

                if flag:
                    # 左下か左上が同じ色なら左にずらす
                    if is_this_color(h+1, w-1, c, N, C) or is_this_color(h-1, w-1, c, N, C):
                        if movable(h, w-1, N, C):
                            C[h][w], C[h][w-1] = C[h][w-1], C[h][w]
                            M_ans.append([h, w, h, w-1])

                    # そうでなく右上が同じなら上にずらす
                    elif is_this_color(h-1, w+1, c, N, C):
                        if movable(h-1, w, N, C):
                            C[h][w], C[h-1][w] = C[h-1][w], C[h][w]
                            M_ans.append([h, w, h-1, w])

    M_ans, C_ans = check_output(M_ans, C_ans, K)
    assert len(M_ans) + len(C_ans) <= K * 100
    return M_ans, C_ans


def check_output(M_ans, C_ans, K):
    if len(M_ans) + len(C_ans) > K * 100:
        C_ans = C_ans[:K*100-len(M_ans)]
    return M_ans, C_ans


def take_input(path=None):
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            N, K = map(int, inputs[0].split())
            C = []
            for i in range(N):
                c = list(map(int, list(inputs[1+i].strip())))
                C.append(c)

    else:
        N, K = NMI()
        C = [list(map(int, list(SI()))) for _ in range(N)]

    return N, K, C


# IS_LOCAL = False

if __name__ == "__main__":
    if IS_LOCAL:
        for i in range(2, 3):
            path = f"./in/{str(i).zfill(4)}.txt"
            M_ans, C_ans = main(*take_input(path))
            outpath = f"./out/{str(i).zfill(4)}.txt"
            output_file(M_ans, C_ans, outpath)

    else:
        M_ans, C_ans = main(*take_input())
        output(M_ans, C_ans)

