import sys
import math
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = NLI()
    B = NLI()
    X = [A[0] ^ b for b in B]
    AC = Counter(A)
    ans = set()
    for x in X:
        BX = [x^b for b in B]
        BC = Counter(BX)
        if AC == BC:
            ans.add(x)

    ans = list(ans)
    ans.sort()
    print(len(ans))
    if len(ans) != 0:
        print(*ans, sep="\n")


if __name__ == "__main__":
    main()
