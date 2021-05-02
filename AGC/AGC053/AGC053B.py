import sys
import math
from collections import deque
import heapq

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
    V = NLI()
    Vt = V[:N][::-1]
    Vb = V[N:]

    hq = []
    heapq.heapify(hq)

    aoki = 0
    for vt, vb in zip(Vt, Vb):
        heapq.heappush(hq, vt)
        heapq.heappush(hq, vb)
        aoki += heapq.heappop(hq)

    print(sum(V) - aoki)


if __name__ == "__main__":
    main()
