import sys
import math
from collections import deque
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def main():
    S = SI()
    l = len(S)
    T = [0] * (l+1)
    inv_S = S[::-1]
    for i, s in enumerate(inv_S):
        s = int(s)
        T[i+1] = (T[i] + s * pow(10, i, 2019)) % 2019
    C = Counter(Counter(T).values())
    ans = 0
    for n, x in C.items():
        if n == 1: continue
        ans += cmb(n, 2) * x
    print(ans)


if __name__ == "__main__":
    main()