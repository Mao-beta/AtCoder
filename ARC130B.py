import sys
import math
from collections import defaultdict

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W, C, Q = NMI()
    TNC = [NLI() for _ in range(Q)]
    ans = [0] * (C+1)
    h = H
    w = W
    H_done = defaultdict(int)
    W_done = defaultdict(int)
    for t, n, c in TNC[::-1]:
        if t == 1 and H_done[n-1] == 0:
            ans[c] += w
            h -= 1
            H_done[n-1] = 1

        elif t == 2 and W_done[n-1] == 0:
            ans[c] += h
            w -= 1
            W_done[n-1] = 1

    print(*ans[1:])


if __name__ == "__main__":
    main()
