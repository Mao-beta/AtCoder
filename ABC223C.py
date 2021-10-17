import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    AB = [NLI() for _ in range(N)]
    L = [0]
    t = 0
    for a, b in AB:
        t += a / b
        L.append(t)
    R = [0]
    t = 0
    for a, b in AB[::-1]:
        t += a / b
        R.append(t)
    R = R[::-1]

    T = L[-1] / 2
    idx = bisect.bisect_left(L, T)

    ans = 0
    for i in range(idx-1):
        ans += AB[i][0]

    T -= L[idx-1]
    ans += AB[idx-1][1] * T
    print(ans)


if __name__ == "__main__":
    main()
