#!/usr/bin/env pypy3
import sys
import math
import bisect
from collections import deque, defaultdict
from heapq import heapify, heappop, heappush


sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    h1 = NI()
    h2 = NI()
    print(h1-h2)



if __name__ == "__main__":
    main()
