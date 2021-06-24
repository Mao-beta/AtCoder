import sys
import math
from collections import Counter
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = [SI() for _ in range(N)]
    ans = Counter(S[0])
    for s in S:
        C = Counter(s)
        for i in range(26):
            x = chr(ord("a") + i)
            k = min(C[x], ans[x])
            ans[x] = k
    ans = sorted(ans.elements())
    print("".join(ans))

if __name__ == "__main__":
    main()
