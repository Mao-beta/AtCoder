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
    N, K = NMI()
    # array_nums[k]はgcd==kとなる数列の数
    array_nums = [0] * (K+1)
    for k in range(K, 0, -1):
        # gcdがkの倍数となる数列
        # == kの倍数のみでできた数列
        num = pow(K//k, N, MOD)
        for i in range(2*k, K+1, k):
            num -= array_nums[i]
        array_nums[k] = num % MOD
    ans = 0
    for i in range(1, K+1):
        ans = (ans + i * array_nums[i]) % MOD
    print(ans)



if __name__ == "__main__":
    main()
