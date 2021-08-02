import sys
import math
from collections import defaultdict
from heapq import heappop, heappush, heapify

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    hq = []
    heapify(hq)
    add = 0
    for q in querys:
        if q[0] == 1:
            heappush(hq, q[1] - add)
        elif q[0] == 2:
            add += q[1]
        else:
            print(heappop(hq) + add)


if __name__ == "__main__":
    main()
