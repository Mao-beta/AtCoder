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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, K = NMI()
    A = NLI()
    A_bit = [0] * 100
    for a in A:
        for i in range(100):
            if (a >> i) & 1:
                A_bit[i] += 1
            else:
                A_bit[i] -= 1

    def dfs(num, i):
        if num > K or i == 100:
            return -1
        res = num
        one = dfs(num, i+1)
        zero = dfs(num + 2**i, i+1)
        if A_bit[i] >= 0 and one <= K:
            res = max(one, res)
        if A_bit[i] <= 0 and zero <= K:
            res = max(zero, res)
        return res

    X = dfs(0, 0)
    ans = 0
    for a in A:
        ans += X^a
    print(ans)




if __name__ == "__main__":
    main()