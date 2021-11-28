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
    S1 = SI()
    S2 = SI()

    if S1 == "..":
        print("Yes")
    elif S1 == ".#":
        if S2 == "#.":
            print("No")
        else:
            print("Yes")
    elif S1 == "#.":
        if S2 == ".#":
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
