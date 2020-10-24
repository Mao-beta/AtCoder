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
    N, M = NMI()
    if N == 1:
        if M == 0:
            print(1, 2)
            exit()
        else:
            print(-1)
            exit()
    if abs(M) >= N - 1:
        print(-1)
        exit()
    if M < 0:
        print(-1)
        exit()
    if M == 0:
        for n in range(N):
            print(2*n+1, 2*n+2)
        exit()

    gap = abs(M)
    ans = []
    ans.append([1, 1+(gap+1)*2])
    for g in range(1, gap+1):
        ans.append([2*g, 2*g+1])
    ans.append([(gap+1)*2, 2+(gap+1)*2])
    now_n = len(ans)
    for i in range(N-now_n):
        ans.append([10**9-1 - i*2, 10**9 - i*2])

    for a in ans:
        print(*a)



if __name__ == "__main__":
    main()
