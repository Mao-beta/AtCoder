import sys
import math
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    Q = NI()
    D = defaultdict(int)
    ans = []
    for _ in range(Q):
        query = NLI()
        if query[0] == 0:
            D[query[1] * 2] = query[2]
        else:
            if query[1] * 2 in D:
                ans.append(D[query[1]*2])
            else:
                ans.append(0)
    print("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
