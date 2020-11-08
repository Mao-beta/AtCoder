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
    A = NLI()
    ans = 2
    now = 0
    for i in range(2, 1001):
        B = [a%i for a in A]
        cnt = B.count(0)
        if now < cnt:
            now = cnt
            ans = i
    print(ans)



if __name__ == "__main__":
    main()
