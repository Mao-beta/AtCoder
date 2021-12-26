import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    XY = [NLI() for _ in range(N)]
    XY.sort(key=lambda x: (x[0], x[1]))

    PQ = defaultdict(int)
    PQ[(0, 0)] = 0
    for i in range(N):
        for j in range(i+1, N):
            xi, yi = XY[i]
            xj, yj = XY[j]

            p = xj - xi
            q = yj - yi

            PQ[(p, q)] += 1

    ans = N - max(PQ.values())
    print(ans)


if __name__ == "__main__":
    main()
