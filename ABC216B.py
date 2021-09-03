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
    names = [SI().split() for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
