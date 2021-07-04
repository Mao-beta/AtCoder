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
    P = NI()
    A = [1]
    for i in range(2, 11):
        A.append(A[-1] * i)
    A = A[::-1]
    ans = 0
    for a in A:
        ans += P // a
        P %= a
    print(ans)


if __name__ == "__main__":
    main()
