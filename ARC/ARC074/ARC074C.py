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


def main():
    H, W = NMI()
    if H % 3 == 0 or W % 3 == 0:
        print(0)
        exit()
    if H == 2 or W == 2:
        print(1)
        exit()

    lh, gh = H // 3, H // 3 + 1
    lw, gw = W // 3, W // 3 + 1

    ans = min(H, W)

    a = lh * W
    b, c = (H - lh) * (W // 2), (H - lh) * (W - W // 2)
    gap = max(a,b,c) - min(a,b,c)
    ans = min(ans, gap)

    a = gh * W
    b, c = (H - gh) * (W // 2), (H - gh) * (W - W // 2)
    gap = max(a,b,c) - min(a,b,c)
    ans = min(ans, gap)

    a = H * lw
    b, c = (W - lw) * (H // 2), (W - lw) * (H - H // 2)
    gap = max(a,b,c) - min(a,b,c)
    ans = min(ans, gap)

    a = H * gw
    b, c = (W - gw) * (H // 2), (W - gw) * (H - H // 2)
    gap = max(a,b,c) - min(a,b,c)
    ans = min(ans, gap)

    print(ans)


if __name__ == "__main__":
    main()