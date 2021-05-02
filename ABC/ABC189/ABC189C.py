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


def largestRectangleArea(A):
    ans = 0
    A = [-1] + A
    A.append(-1)
    n = len(A)
    stack = [0]  # store index

    for i in range(n):
        while A[i] < A[stack[-1]]:
            h = A[stack.pop()]
            area = h*(i-stack[-1]-1)
            ans = max(ans, area)
        stack.append(i)
    return ans


def main():
    N = NI()
    A = NLI()
    print(largestRectangleArea(A))


if __name__ == "__main__":
    main()
