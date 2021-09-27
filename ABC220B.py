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
        res = str(m) + res
        tmp //= base1
    return res or "0"


def main():
    K = NI()
    A, B = SI().split()
    A = convert_base(A, K, 10)
    B = convert_base(B, K, 10)
    print(int(A)*int(B))


if __name__ == "__main__":
    main()
