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
    A = NLI()
    B = NLI()
    ans = []
    post = []
    ai = 0
    for i in range(N):
        b = B[i]
        if b <= A[ai]:
            post.append(b)
        else:
            ans.append(b)
            ai += 1

    for a, b in zip(A, ans+post):
        if a == b:
            print("No")
            exit()

    print("Yes")
    print(*(ans+post))





if __name__ == "__main__":
    main()