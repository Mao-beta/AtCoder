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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    S, T = SI().split()
    if S[0] == "B" and T[0] == "B":
        print(abs(int(S[1]) - int(T[1])))
        exit()
    if S[1] == "F" and T[1] == "F":
        print(abs(int(S[0]) - int(T[0])))
        exit()
    if S[1] == "F" and T[0] == "B":
        print(int(S[0]) + int(T[1]) - 1)
        exit()
    if S[0] == "B" and T[1] == "F":
        print(int(S[1]) + int(T[0]) - 1)
        exit()


if __name__ == "__main__":
    main()