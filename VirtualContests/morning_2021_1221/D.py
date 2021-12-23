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
    N = NI()

    # 約数列挙（単体）
    def divisors(x):
        res = set()
        ans = 0
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                m = x // i - 1
                if m <= i:
                    break
                ans += m

                res.add(i)
                res.add(x // i)
        return ans

    print(divisors(N))


if __name__ == "__main__":
    main()
