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
    N, M = NMI()
    S = NLI()
    T = NLI()
    if (1 not in S) and (1 in T):
        print(-1)
        exit()
    if (0 not in S) and (0 in T):
        print(-1)
        exit()
    if len(set(T)) == 1:
        t = T[0]
        rb = 1 + S[::-1].index(t)
        lb = S.index(t)
        bb = min(rb, lb)
        ans = M + bb
        print(ans)
        exit()


    a = S[0]
    b = 1 - a
    rb = 1 + S[::-1].index(b)
    lb = S.index(b)
    bb = min(rb, lb)

    ans = M
    is_start = True
    now = a
    for t in T:
        if t == now:
            ans += 0
        elif is_start:
            ans += bb
            now = 1 - now
            is_start = False
        else:
            ans += 1
            now = 1 - now
    print(ans)


if __name__ == "__main__":
    main()
