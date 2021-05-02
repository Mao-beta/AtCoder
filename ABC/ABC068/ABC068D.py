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
    K = NI()
    N = 50
    X = K // N
    Y = K % N
    A = [N-1+X] * N
    for y in range(Y):
        A = [a-1 for a in A]
        A[y] += N+1
    print(N)
    print(*A)


if __name__ == "__main__":
    main()
