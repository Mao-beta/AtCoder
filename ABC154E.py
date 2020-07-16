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
    N = SI()
    max_keta = len(N)
    K = NI()

    # 桁dp dp[now_k][keta]は
    # keta文字目まで確定で0以外がnow_k個ある場合の数
    dp_small = [[0] * (max_keta + 1) for i in range(K + 1)]
    dp_same = [[0] * (max_keta + 1) for i in range(K + 1)]
    dp_same[0][0] = 1
    for keta in range(max_keta-1):
        for now_k in range(K+1):
            for i in range(10):
                if i == 0:
                    dp_small[now_k][keta+1] += dp_small[now_k][keta]
                    continue
                if now_k == K:
                    continue
                dp_small[now_k+1][keta + 1] += dp_small[now_k][keta]

            limit_num = int(N[keta+1])
            for i in range(limit_num+1):
                if i == limit_num and i == 0:
                    dp_same[now_k][keta+1] += dp_same[now_k][keta]
                    continue
                if i == 0:
                    dp_small[now_k][keta + 1] += dp_same[now_k][keta]
                    continue
                if i == limit_num:
                    if now_k < K:
                        dp_same[now_k+1][keta + 1] += dp_same[now_k][keta]
                    continue
                if now_k < K:
                    dp_same[now_k + 1][keta + 1] += dp_same[now_k][keta]
    print(dp_small)
    print(dp_same)
    print(dp_small[K][max_keta] + dp_same[K][max_keta])

if __name__ == "__main__":
    main()