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
    A = [-1] * (N+1)
    max_A = -1
    for i in range(N, 0, -1):
        ng_num = set()
        all_num = set(range(1, max_A + 3))
        for j in range(2*i, N+1, i):
            ng_num.add(A[j])
        A[i] = min(all_num - ng_num)
        max_A = max(max_A, A[i])

    print(*A[1:])


if __name__ == "__main__":
    main()
