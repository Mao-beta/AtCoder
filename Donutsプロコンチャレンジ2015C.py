import sys
import math
from collections import deque
import heapq as hq

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
    H = NLI()
    able = []
    hq.heapify(able)
    for i, h in enumerate(H):
        print(len(able))
        while able:
            q = hq.heappop(able)
            if q > h:
                hq.heappush(able, q)
                break
        hq.heappush(able, h)


if __name__ == "__main__":
    main()