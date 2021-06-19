import sys
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
    C = Counter(NLI())
    ans = N * (N-1) // 2
    for _, k in C.items():
        ans -= k * (k-1) // 2
    print(ans)


if __name__ == "__main__":
    main()
