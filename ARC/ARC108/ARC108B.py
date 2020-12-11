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
    N = NI()
    S = SI()
    stack = deque()
    for s in S:
        stack.append(s)
        if len(stack) <= 2: continue
        if stack[-3] == "f" and stack[-2] == "o" and stack[-1] == "x":
            stack.pop()
            stack.pop()
            stack.pop()
            N -= 3
    print(N)



if __name__ == "__main__":
    main()
