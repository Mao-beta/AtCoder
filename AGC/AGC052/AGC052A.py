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
    T = NI()
    for _ in range(T):
        N = NI()
        S1 = SI()*2
        S2 = SI()*2
        S3 = SI()*2

        now = 0
        ans1 = set()
        for s in S1:
            if s == "1":
                now += 1
            else:
                ans1.add(now)

        now = 0
        ans2 = set()
        for s in S2:
            if s == "1":
                now += 1
            else:
                ans2.add(now)

        now = 0
        ans3 = set()
        for s in S3:
            if s == "1":
                now += 1
            else:
                ans3.add(now)

        inter = ans1 & ans2 & ans3

        if inter:
            k = inter.pop()
            print("1"*k + "0" + "1"*(2*N-k))
            continue

        now = 0
        ans1 = set()
        for s in S1:
            if s == "0":
                now += 1
            else:
                ans1.add(now)

        now = 0
        ans2 = set()
        for s in S2:
            if s == "0":
                now += 1
            else:
                ans2.add(now)

        now = 0
        ans3 = set()
        for s in S3:
            if s == "0":
                now += 1
            else:
                ans3.add(now)

        inter = ans1 & ans2 & ans3
        if inter:
            k = inter.pop()
            print("0"*k + "1" + "0"*(2*N-k))
            continue


if __name__ == "__main__":
    main()
