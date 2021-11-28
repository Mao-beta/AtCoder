import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()



def main():
    N, M = NMI()
    AB = [NLI() for _ in range(M)]
    AB.sort(key=lambda x: (x[0], -x[1]))
    INF = 10**8
    Y = [INF] * (N+1)
    Y[0] = 0
    for a, b in AB:
        idx = bisect.bisect_left(Y, b)
        Y[idx] = min(Y[idx], b)

    ans = bisect.bisect_left(Y, INF) - 1

    print(ans)


if __name__ == "__main__":
    main()
