import sys
import math
from heapq import heappop, heappush, heapify

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    AB = [NLI() for _ in range(N)]

    hq = []
    heapify(hq)

    for a, b in AB:
        heappush(hq, (-b, a-b))

    ans = 0
    for _ in range(K):
        p, g = heappop(hq)
        ans += -p
        heappush(hq, (-g, 0))

    print(ans)


if __name__ == "__main__":
    main()
