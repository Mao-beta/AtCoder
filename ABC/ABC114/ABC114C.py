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

ans = 0

def main():
    N = NI()

    def dfs(num):
        global ans
        if "3" in str(num) and "5" in str(num) and "7" in str(num):
            ans += 1
        if num * 10 + 3 <= N:
            dfs(num * 10 + 3)
        if num * 10 + 5 <= N:
            dfs(num * 10 + 5)
        if num * 10 + 7 <= N:
            dfs(num * 10 + 7)

    dfs(0)
    print(ans)

if __name__ == "__main__":
    main()