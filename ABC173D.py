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
    A = NLI()
    A = [a * (-1) for a in A]
    A.sort()
    C = []
    heapq.heapify(C)
    ans = 0
    for i, a in enumerate(A):
        if i == 0:
            heapq.heappush(C, a)
            continue

        ans -= heapq.heappop(C)
        heapq.heappush(C, a)
        heapq.heappush(C, a)
    print(ans)


if __name__ == "__main__":
    main()