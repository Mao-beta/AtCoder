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
    ans = set()
    for i in range(1, 10**6+1):
        if N % i == 0:
            ans.add(i)
            ans.add(N//i)
    ans = sorted(list(ans))
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
