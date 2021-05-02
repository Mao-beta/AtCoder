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
    S = SI()
    ans = 0
    prev = S[0]
    plus = 0
    ng = ""
    for i, s in enumerate(S):
        if i == 0:
            continue

        if s != prev:
            if ng != s:
                ans += plus
            else:
                ans += max(plus - 1, 0)
        else:
            if ng != s:
                ans += plus
                plus += 1
                ng = s
            else:
                ans += max(plus - 1, 0)

        prev = s
    print(ans)

if __name__ == "__main__":
    main()
