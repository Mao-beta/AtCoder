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


def main():
    S = SI()
    D = deque()
    is_rev = False
    for s in S:
        if s == "R":
            is_rev = not is_rev
            continue

        if len(D) == 0:
            D.append(s)
            continue

        if not is_rev:
            a = D.pop()
            if a != s:
                D.append(a)
                D.append(s)
        else:
            a = D.popleft()
            if a != s:
                D.appendleft(a)
                D.appendleft(s)

    if is_rev:
        D = reversed(D)

    print("".join(D))


if __name__ == "__main__":
    main()
