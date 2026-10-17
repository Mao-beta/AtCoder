import sys
import math
from collections import defaultdict
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
    if S[3] != "-":
        print("No")
        exit()

    try:
        a = int(S[0:3])
        b = int(S[4:])
    except:
        print("No")
        exit()

    print("Yes")


if __name__ == "__main__":
    main()
