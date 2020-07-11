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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    T = NI()
    A = []
    for _ in range(T):
        N = NI()
        camels_L = []
        camels_R = []
        camels_N = []
        for _ in range(N):
            k, l, r = NMI()
            if l > r:
                camels_L.append([k-1, -l, -r])
            elif r > l:
                camels_R.append([k-1, -l, -r])
            else:
                camels_N.append([k-1, -l, -r])
        camels_L.sort()
        camels_R.sort(reverse=True)
        L_heap = []
        R_heap = []
        heapq.heapify(L_heap)
        heapq.heapify(R_heap)
        print(camels_L)
        print(camels_R)







if __name__ == "__main__":
    main()