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
    S = SI()
    R = S[::-1]
    N = len(S)
    if N == 1:
        print(0)
        exit()
    if S == R:
        print(N//2 * 25 * 2)
        exit()

    cnt = 0
    for s, r in zip(S, R):
        if s != r:
            cnt += 1
    if cnt == 2:
        print(25*N - cnt)
    else:
        print(25*N)

if __name__ == "__main__":
    main()