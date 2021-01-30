import sys
import math
from collections import deque
from itertools import product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M = NMI()
    AB = [NLI() for _ in range(M)]
    K = NI()
    CD = [NLI() for _ in range(K)]

    ans = 0
    cases = list(product([0, 1], repeat=K))
    for case in cases:
        dishes = [0] * N
        for i, choice in enumerate(case):
            target = CD[i][choice] - 1
            dishes[target] = 1
        res = 0
        for a, b in AB:
            a, b = a-1, b-1
            if dishes[a] and dishes[b]:
                res += 1

        ans = max(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
