import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()

    S = sum(A)
    if S % 10:
        print("No")
        exit()

    X = S // 10

    AA = A + A
    que = deque()
    now = 0
    for a in AA:
        while que and now > X:
            d = que.popleft()
            now -= d

        if now < X:
            que.append(a)
            now += a

        if now == X:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
