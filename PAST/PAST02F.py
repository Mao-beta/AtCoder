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
    N = NI()
    tasks = [NLI() for _ in range(N)]
    tasks.sort()
    hq = []
    ans = 0
    idx = 0
    for i in range(1, N+1):
        if idx < N:
            while tasks[idx][0] <= i and idx < N:
                heapq.heappush(hq, tasks[idx][1] * (-1))
                idx += 1
                if idx >= N:
                    break
        ans += heapq.heappop(hq) * (-1)
        print(ans)



if __name__ == "__main__":
    main()