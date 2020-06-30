import sys
import math
from collections import deque
import heapq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = []
    for i in range(N):
        a, b = NMI()
        A.append([a, b])
    A.sort(key=lambda x: x[1])
    t = 0
    for a in A:
        t += a[0]
        if t > a[1]:
            print("No")
            exit()

    print("Yes")



if __name__ == "__main__":
    main()