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
    L = NI()
    if L <= 8:
        print(0)
        exit()
    m = L - L % 4
    n = m // 4 - 1
    ans = 2*(n%MOD)**2 + (n%MOD)
    tmp = [1, 1, 0, 1]
    for i in range(1, L%4+1):
        ans += (n%MOD) + tmp[i]
    ans -= (L%MOD) - 5
    print(ans%MOD)


if __name__ == "__main__":
    main()