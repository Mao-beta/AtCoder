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
    t, N = NMI()
    y = (100+t)
    S = set(range(1, y+1))
    for i in range(1, 101):
        S.discard((100+t)*i//100)

    k = len(S)
    ans = N//k * y
    m = N % k
    if m == 0:
        print(ans - y + max(S))
        exit()

    ans += sorted(list(S))[m-1]
    print(ans)


if __name__ == "__main__":
    main()
