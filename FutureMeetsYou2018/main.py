import sys
import math
from collections import deque

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


def solve(N, K, A):
    ans = []

    for _ in range(K):
        ans.append([1, 1, 2, 2, 0])

    return ans






def output(ans):
    for row in ans:
        print(*row)


def input_values(path=None):
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            N, K = map(int, inputs[0].split())
            A = [int(row) for row in inputs[1:]]

    else:
        N, K = NMI()
        A = [NI() for _ in range(N)]
    return N, K, A


def main():
    path = None
    if IS_LOCAL:
        path = "./in/in_K1050.txt"

    N, K, A = input_values(path)
    ans = solve(N, K, A)
    output(ans)


if __name__ == "__main__":
    main()
