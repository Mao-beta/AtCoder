import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    T = NI()
    for _ in range(T):
        a, b, c = NMI()
        b //= 2
        ans = 0
        if b >= c:
            ans += c
            if a//2 >= b-c:
                ans += b-c + (a-2*b+2*c)//5
            else:
                ans += a//2

        else:
            ans += b
            if a >= (c-b)//2:
                ans += (c-b)//2
                if a-(c-b)//2 >= 3 and (c-b)%2:
                    ans += 1 + (a-(c-b)//2-3)//5
                else:
                    ans += (a-(c-b)//2)//5

            else:
                ans += a

        print(ans)


if __name__ == "__main__":
    main()
