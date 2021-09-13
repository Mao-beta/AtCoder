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
    N, K = NMI()
    if N == 0:
        print(0)
        exit()
    N = str(N)

    def convert_base(str_n, base0, base1):
        """
        base0進数の文字列str_nを、base1進数の文字列に変換する
        """
        tmp = 0
        for i, n in enumerate(str_n[::-1]):
            tmp += pow(base0, i) * int(n)

        res = ""
        while tmp > 0:
            m = tmp % base1
            if m == 8:
                m = 5
            res = str(m) + res
            tmp //= base1
        return res or "0"

    for _ in range(K):
        N = convert_base(N, 8, 9)
    print(N)


if __name__ == "__main__":
    main()
