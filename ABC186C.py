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
    ans = 0
    for i in range(1, N+1):
        if "7" in str(i):
            continue
        flag = True
        while i > 0:
            num = i % 8
            if num == 7:
                flag = False
            i //= 8
        if flag:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
