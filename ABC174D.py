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
    S = SI()
    l = 0
    r = N - 1
    ans = 0
    if S.count("R") == 0 or S.count("R") == N:
        print(0)
        exit()

    while r - l >= 1:
        if S[l] == "W" and S[r] == "R":
            ans += 1
            l += 1
            r -= 1
        elif S[l] == "W":
            r -= 1
        elif S[r] == "R":
            l += 1
        else:
            l += 1
            r -= 1

    print(ans)


if __name__ == "__main__":
    main()