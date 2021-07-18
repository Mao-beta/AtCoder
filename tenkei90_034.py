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
    A = NLI()

    que = deque()
    D = defaultdict(int)
    kind = 0
    ans = 0

    for i, a in enumerate(A):
        que.append(a)
        D[a] += 1
        if D[a] == 1:
            kind += 1

        while kind > K:
            x = que.popleft()
            D[x] -= 1
            if D[x] == 0:
                kind -= 1

        ans = max(ans, len(que))

    print(ans)


if __name__ == "__main__":
    main()
