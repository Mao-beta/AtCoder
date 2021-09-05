import sys
from heapq import heappop, heappush
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    Q = NI()
    wait = deque()
    hq = []
    for _ in range(Q):
        query = NLI()
        if query[0] == 1:
            wait.append(query[1])
        elif query[0] == 2:
            if hq:
                m = heappop(hq)
                print(m)
            else:
                m = wait.popleft()
                print(m)

        else:
            while wait:
                heappush(hq, wait.popleft())
            wait = deque()


if __name__ == "__main__":
    main()
