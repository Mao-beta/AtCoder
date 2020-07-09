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
    N = NI()
    grid = make_grid(10, 10, 0)
    ans = 0
    for i in range(N+1):
        s = str(i)
        t = int(s[0])
        b = int(s[-1])
        grid[t][b] += 1
    for i in range(1, 10):
        for j in range(1, 10):
            ans += grid[i][j] * grid[j][i]
    print(ans)


if __name__ == "__main__":
    main()