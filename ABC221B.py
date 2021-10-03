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
    S = SI()
    T = SI()

    if S == T:
        print("Yes")
    else:
        for i in range(len(S)-1):
            SS = list(S)
            SS[i], SS[i+1] = SS[i+1], SS[i]
            SS = "".join(SS)
            if SS == T:
                print("Yes")
                exit()
        print("No")


if __name__ == "__main__":
    main()
