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



def solve(N, K, A):
    ans = []
    gaps = [(a-i, i) for i, a in enumerate(A, start=1)]
    P = []
    M = []
    heapify(P)
    heapify(M)

    for g, i in gaps:
        if g >= 0:
            heappush(P, (-g, i))
        else:
            heappush(M, (g, i))


    for _ in range(K):
        pg, pi = heappop(P)
        pg *= -1
        mg, mi = heappop(M)

        v = min(abs(pg), abs(mg))
        heappush(P, (-pg+v, pi))
        heappush(M, (mg+v, mi))

        ans.append([pi, pi, mi, mi, v])

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
        path = Path("./in/in_K3000.txt")
        filename = path.name.split("_")[1]

    N, K, A = input_values(path)
    ans = solve(N, K, A)
    if IS_LOCAL:
        with open(f"./out/out_{filename}", "w") as f:
            for row in ans:
                f.write(" ".join(map(str, row)) + "\n")

    output(ans)


if __name__ == "__main__":
    main()
