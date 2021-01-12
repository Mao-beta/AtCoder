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
    N, M = NMI()
    A = NLI()
    min_bits = set(a&(-a) for a in A)

    if len(min_bits) != 1:
        print(0)
        exit()

    lcm = 1
    for a in A:
        g = math.gcd(a, lcm)
        lcm = a * lcm // g
        if lcm > 2 * M:
            print(0)
            exit()

    half = lcm // 2
    print(M // half - M // lcm)


if __name__ == "__main__":
    main()
