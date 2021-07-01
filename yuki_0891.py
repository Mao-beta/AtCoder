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
    N = NI()
    A, B, C = NMI()
    AB = A*B//math.gcd(A, B)
    BC = B*C // math.gcd(B, C)
    CA = C*A // math.gcd(C, A)
    ABC = AB*C // math.gcd(AB, C)

    ans = N // A + N // B + N // C
    ans -= N // AB + N // BC + N // CA
    ans += N // ABC
    print(ans)


if __name__ == "__main__":
    main()
