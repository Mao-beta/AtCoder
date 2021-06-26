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
    N = NI()
    LRT = []
    for _ in range(N):
        t, l, r = NMI()
        LRT.append([l, r, t])
    LRT.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            li, ri, ti = LRT[i]
            lj, rj, tj = LRT[j]

            if ti in [1, 3]:
                if tj in [3, 4]:
                    if lj < ri:
                        ans += 1
                else:
                    if lj <= ri:
                        ans += 1

            if ti in [2, 4]:
                if tj in [3, 4]:
                    if lj < ri:
                        ans += 1
                else:
                    if lj < ri:
                        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
