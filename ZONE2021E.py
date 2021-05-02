import sys
import math
from collections import deque
from heapq import heappush, heappop, heapify

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()




def main():
    R, C = NMI()
    A = [NLI() for _ in range(R)]
    B = [NLI() for _ in range(R-1)]

    hq = []
    heapify(hq)
    heappush(hq, (0, 0))
    seen = [0] * (R*C)
    temp_dist = [10**15] * (R*C)

    while hq:
        now, p = heappop(hq)
        h, w = p // C, p % C
        if seen[p]:
            continue

        seen[p] = 1
        temp_dist[p] = now
        if h == R-1 and w == C-1:
            print(now)
            exit()

        if w < C-1:
            a = A[h][w]
            if not seen[p+1]:
                heappush(hq, (now + a, p+1))
                temp_dist[p+1] = min(temp_dist[p+1], now+a)
        if w > 0:
            a = A[h][w-1]
            if not seen[p-1]:
                heappush(hq, (now + a, p-1))
                temp_dist[p-1] = min(temp_dist[p-1], now + a)
        if h < R-1:
            b = B[h][w]
            if not seen[p+C]:
                heappush(hq, (now + b, p+C))
                temp_dist[p+C] = min(temp_dist[p+C], now + b)
        if h > 0:
            for i in range(1, h+1):
                if not seen[p-i*C] and temp_dist[p-i*C] > now+i+1:
                    heappush(hq, (now + i + 1, p-i*C))
                    temp_dist[p-i*C] = min(temp_dist[p-i*C], now + i + 1)


if __name__ == "__main__":
    main()
