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
    S = SI()
    if S[0] != S[-1]:
        print(1)
        exit()

    a = S[0]
    for i, s in enumerate(S):
        if i == N-1:
            continue
        if S[i+1] != a and S[i] != a:
            print(2)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
