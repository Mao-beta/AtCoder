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
    N, M = NMI()
    A = NLI()
    A = [-a for a in A]
    heapq.heapify(A)
    for i in range(M):
        a_max = -heapq.heappop(A)
        a_max = a_max // 2
        heapq.heappush(A, -a_max)
    print(-sum(A))



if __name__ == "__main__":
    main()