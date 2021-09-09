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
    N, K = NMI()
    M = (N-1)*(N-2)//2
    if K > M:
        print(-1)
        exit()
    rem = M - K
    ans = []
    for i in range(2, N+1):
        ans.append((1, i))
    for i in range(2, N+1):
        for j in range(i+1, N+1):
            if rem > 0:
                ans.append((i, j))
                rem -= 1
    print(len(ans))
    for i, j in ans:
        print(i, j)


if __name__ == "__main__":
    main()
