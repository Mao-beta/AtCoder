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
    X, Y = NMI()
    if X >= Y:
        print(X-Y)
        exit()

    already = set()
    queue = deque()
    queue.append((0, Y))
    over = 10**20
    while queue:
        cnt, now = queue.popleft()
        already.add(now)
        if now > X:
            over = min(over, cnt + (now-X))

        if now == X:
            print(min(cnt, over))
            exit()

        if now-1 not in already:
            queue.append((cnt+1, now-1))
        if now+1 not in already:
            queue.append((cnt+1, now+1))
        if now % 2 == 0:
            if now // 2 not in already:
                queue.append((cnt+1, now//2))


if __name__ == "__main__":
    main()
