import sys
import math
from collections import deque
from pathlib import Path
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False


def solve(values):
    N, M, L, S = values

    ans = [["."]*M for _ in range(M)]
    for h in range(M):
        ans[h][0] = "#"
        ans[h][-1] = "#"
    for w in range(M):
        ans[0][w] = "#"
        ans[-1][w] = "#"

    return ans



def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write("".join(map(str, row)) + "\n")
    else:
        for row in ans:
            print(*row, sep="")


def input_values(path=None):
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            N, M, L = map(int, inputs[0].split())
            S = inputs[1:]

    else:
        N, M, L = NMI()
        S = [SI() for _ in range(N)]

    return N, M, L, S


def main(file=None):
    in_path = None
    out_path = None

    if file:
        in_filename = file + ".in"
        in_path = Path("./in/") / in_filename
        out_filename = file + ".out"
        out_path = Path("./out/") / out_filename

    values = input_values(in_path)
    ans = solve(values)
    output_ans(ans, out_path)


if __name__ == "__main__":
    if IS_LOCAL:
        for i in range(100):
            main(str(i).zfill(3))
    else:
        main()
