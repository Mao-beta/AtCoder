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
    LR = [NLI() for _ in range(N)]
    now_lr = [-10**10, 10**10]

    for l, r in LR:
        nl, nr = now_lr
        nl = max(nl, l)
        nr = min(nr, r)
        now_lr[0] = nl
        now_lr[1] = nr
        ans = math.ceil((nl - nr)/2)
        print(max(0, ans))


if __name__ == "__main__":
    main()
