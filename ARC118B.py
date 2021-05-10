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
    K, N, M = NMI()
    A = NLI()
    A = [M*a for a in A]
    B = [a//N * N for a in A]
    R = [b-a for a, b in zip(A, B)]
    rem = M - sum(B)//N
    BB = [(r, i) for i, r in enumerate(R)]
    heapq.heapify(BB)
    for i in range(rem):
        r, i = heapq.heappop(BB)
        B[i] += N
    B = [b//N for b in B]
    print(*B)


if __name__ == "__main__":
    main()
