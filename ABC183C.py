import sys
import math
from collections import deque
from itertools import permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, K = NMI()
    T = [NLI() for _ in range(N)]
    case = permutations(range(1, N), N-1)
    case = [[0]+list(c)+[0] for c in case]
    ans = 0
    for c in case:
        time = 0
        for i in range(N):
            x, y = c[i], c[i+1]
            time += T[x][y]
        if time == K:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
