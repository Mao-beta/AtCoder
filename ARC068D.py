import sys
import math
from collections import defaultdict
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
    cnts = [0] * (10**5+1)
    for a in A:
        cnts[a] += 1
        if cnts[a] >= 3:
            cnts[a] -= 2
    hold = None
    for i, c in enumerate(cnts):
        if c <= 1:
            continue
        if hold:
            cnts[hold] -= 1
            cnts[i] -= 1
            hold = None
        else:
            hold = i
    ans = sum(cnts)
    print(ans-2 if hold else ans)


if __name__ == "__main__":
    main()
