import sys
import math
from collections import deque
from heapq import heapify, heappop, heappush

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, D = NMI()
    LR = [NLI() for _ in range(N)]
    broken_L = -1
    hq = []
    heapify(hq)
    for l, r in LR:
        heappush(hq, (r, l))

    ans = 0
    while hq:
        r, l = heappop(hq)
        if l <= broken_L:
            continue

        broken_L = r + D - 1
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
