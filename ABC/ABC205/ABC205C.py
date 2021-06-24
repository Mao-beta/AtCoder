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
    A, B, C = NMI()
    if A >= 0 and B >= 0:
        if A > B:
            print(">")
        elif A < B:
            print("<")
        else:
            print("=")

    elif A >= 0 and B < 0:
        if C % 2:
            print(">")
        else:
            B *= -1
            if A > B:
                print(">")
            elif A < B:
                print("<")
            else:
                print("=")

    elif A < 0 and B >= 0:
        if C % 2:
            print("<")
        else:
            A *= -1
            if A > B:
                print(">")
            elif A < B:
                print("<")
            else:
                print("=")

    else:
        if C % 2:
            A *= -1
            B *= -1
            if A > B:
                print("<")
            elif A < B:
                print(">")
            else:
                print("=")
        else:
            A *= -1
            B *= -1
            if A > B:
                print(">")
            elif A < B:
                print("<")
            else:
                print("=")


if __name__ == "__main__":
    main()
