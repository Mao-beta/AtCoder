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
    ans = []

    return ans



def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write(" ".join(map(str, row)) + "\n")
    else:
        for row in ans:
            print(*row)


def input_values(path=None):
    values = {}
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            N, K = map(int, inputs[0].split())
            A = [int(row) for row in inputs[1:]]

    else:
        N, K = NMI()
        A = [NI() for _ in range(N)]

    return values


def main():
    in_path = None
    if IS_LOCAL:
        in_path = Path("./in/in_K3000.txt")
        filename = in_path.name.split("_")[1]

    values = input_values(in_path)
    ans = solve(values)

    out_path = None
    if IS_LOCAL:
        out_path = Path("./out/")/filename

    output_ans(ans, out_path)


if __name__ == "__main__":
    main()
