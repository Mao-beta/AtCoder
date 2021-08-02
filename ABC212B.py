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
    X = SI()
    if len(set(X)) == 1:
        print("Weak")
        exit()

    X = list(map(int, X))
    if X[0]%10 == (X[1]-1)%10 and X[1]%10 == (X[2]-1)%10 and X[2]%10 == (X[3]-1)%10:
        print("Weak")
    else:
        print("Strong")


if __name__ == "__main__":
    main()
