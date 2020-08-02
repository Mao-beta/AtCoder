import sys
import math
from collections import deque

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
    A = NLI()
    combos = []
    for m in range(M):
        b, c, *I = NMI()
        members = 0
        for i in I:
            members += 2**(i-1)
        combos.append([b, c, members])

    units = range(2**N)
    ans = 0
    for unit in units:
        if bin(unit).count("1") != 9:
            continue

        score = 0
        for i in range(N):
            if (unit >> i) & 1:
                score += A[i]

        for combo in combos:
            if bin(combo[2] & unit).count("1") >= 3:
                score += combo[0]
        ans = max(ans, score)

    print(ans)


if __name__ == "__main__":
    main()