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
    S = []
    T = []
    for i in range(N):
        s, t = SI().split()
        S.append(s)
        T.append((int(t), i))
    T.sort()
    idx = T[-2][1]
    print(S[idx])


if __name__ == "__main__":
    main()
