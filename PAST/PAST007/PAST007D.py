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
    S = list(SI())
    if N <= 2:
        print("".join(S))
        exit()

    for i in range(N-2):
        X = S[i] + S[i+1] + S[i+2]
        if X in ["axa", "ixi", "uxu", "exe", "oxo"]:
            S[i] = "."
            S[i+1] = "."
            S[i+2] = "."

    print("".join(S))


if __name__ == "__main__":
    main()
