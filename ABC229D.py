import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = SI()
    K = NI()
    que = deque()
    ans = 0
    use = 0

    for s in S:
        que.append(s)
        if s == ".":
            use += 1

        while que and use > K:
            rm = que.popleft()
            if rm == ".":
                use -= 1

        ans = max(ans, len(que))

    print(ans)


if __name__ == "__main__":
    main()
