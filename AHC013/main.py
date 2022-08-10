import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations


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

    def move(self, d):
        self.h += DH[d]
        self.w += DW[d]

    def __str__(self):
        return f"CPU{str(self.idx).zfill(3)} h: {self.h}, w: {self.w}, k: {self.k}"


class Pipe:
    def __init__(self, px, py, qx, qy):
        self.P = [px, py]
        self.Q = [qx, qy]


class AllPipes:
    def __init__(self, N):
        self.N = N
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


def _main(N, K, C):
    M_ans = []
    C_ans = []

    # CPUを初期化
    CPUs = []
    idx = 0
    for h in range(N):
        for w in range(N):
            if C[h][w] != 0:
                CPUs.append(CPU(h, w, C[h][w], idx))
                idx += 1

    # つなげるだけPipeをつなぐ

    # あるCPUに注目し、隣接マスに同じ色のPipeがあればのっかる
    # つまり、盤面を見たらそこがどのCPUとどのCPUのPipe上か高速に知れたらよい


    print(*CPUs, sep="\n")

    return M_ans, C_ans


def movable(h, w, N, C):
    return on_board(h, w, N) and C[h][w] == 0


def is_this_color(h, w, c, N, C):
    return on_board(h, w, N) and C[h][w] == c


def main(N, K, C):
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
        for i in range(100):
            path = f"./in/{str(i).zfill(4)}.txt"
            M_ans, C_ans = main(*take_input(path))
            outpath = f"./out/{str(i).zfill(4)}.txt"
            output_file(M_ans, C_ans, outpath)

    else:
        M_ans, C_ans = main(*take_input())
        output(M_ans, C_ans)

