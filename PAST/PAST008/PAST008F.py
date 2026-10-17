import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = SI()
    if S.count("0") == 1:
        print(-1)
        exit()

    ans = list(range(1, N+1))

    if S.count("0") == 0:
        print(*ans)
        exit()

    hold = -1
    first = -1
    for i, d in enumerate(S, start=1):
        if d == "1":
            continue

        if hold == -1:
            hold = i
            first = i
        else:
            ans[i-1] = hold
            hold = i

    ans[first-1] = hold
    print(*ans)


if __name__ == "__main__":
    main()
