import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
from pathlib import Path
import random

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


def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write("".join(map(str, row)) + "\n")
    else:
        for row in ans:
            print(*row)


def main():
    dst_dir = Path("./in/")
    dst_dir.mkdir(exist_ok=True)

    T = 100

    for case in range(T):
        random.seed(case)
        filename = str(case).zfill(3) + ".in"

        lines = []

        N = random.randint(10, 20)
        M = random.randint(5, 10)

        XY = set()
        for x in range(1, 31):
            for y in range(1, 31):
                XY.add((x, y))

        lines.append(str(N))

        for _ in range(N):
            px, py = XY.pop()
            pt = random.randint(1, 5)
            lines.append(f"{px} {py} {pt}")

        lines.append(str(M))

        for _ in range(M):
            hx, hy = XY.pop()
            lines.append(f"{hx} {hy}")

        output_ans(lines, dst_dir/filename)


if __name__ == "__main__":
    main()
