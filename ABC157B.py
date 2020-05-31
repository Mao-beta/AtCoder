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
    A = [NLI() for _ in range(3)]
    N = NI()
    B = [NI() for _ in range(N)]
    hit = [[0]*3 for _ in range(3)]
    for b in B:
        for i in range(3):
            for j in range(3):
                if b == A[i][j]:
                    hit[i][j] = 1

    for h in hit:
        if sum(h) == 3:
            print("Yes")
            exit()
    for j in range(3):
        if hit[0][j] + hit[1][j] + hit[2][j] == 3:
            print("Yes")
            exit()
    if hit[0][2] + hit[1][1] + hit[2][0] == 3:
        print("Yes")
        exit()
    if hit[0][0] + hit[1][1] + hit[2][2] == 3:
        print("Yes")
        exit()
    print("No")



if __name__ == "__main__":
    main()