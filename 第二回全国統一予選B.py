import sys
import math
from collections import defaultdict
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    D = NLI()
    if D[0] != 0:
        print(0)
        exit()

    C = Counter(D)
    V = 0
    ans = 1
    for d in range(N):
        v = C.get(d)
        if v:
            V += v
            if d == 0 and v != 1:
                print(0)
                exit()
            elif d == 0 or d == 1:
                pass
            else:
                pv = C.get(d-1)
                ans *= pow(pv, v, MOD)
                ans %= MOD
        else:
            break
    if V == N:
        print(ans)
    else:
        print(0)


if __name__ == "__main__":
    main()
