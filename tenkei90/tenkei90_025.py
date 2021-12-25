import sys
import random
from functools import lru_cache

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def mul(x):
    res = 1
    while x > 0:
        res *= x % 10
        x //= 10
    return res


def solve_lazy(N, B):
    ans = 0
    for m in range(N+1):
        if m - mul(m) == B:
            print("lm:", m, "lf(m)", mul(m))
            ans += 1
    return ans


def solve(N, B):
    # 2, 3, 5, 7の積を M として、N-B以下の M を全探索
    # それぞれのMについて、M+Bの各位の積が M と一致するか？

    # 2: 30以下、3: 20以下、5: 10以下、7: 10以下
    P = [2, 3, 5, 7]
    D = [30, 20, 10, 10]

    ans = [0]

    if N < B:
        return 0

    @lru_cache(maxsize=None)
    def rec(now, dep):
        #print(now, dep)
        if dep == len(D):
            if now == mul(now + B):
                #print("m:", now+B, "f(m):", now)
                ans[0] += 1
            return

        p = P[dep]
        d = D[dep]

        for i in range(d + 1):
            if now > N - B:
                break
            rec(now, dep + 1)
            now *= p

    rec(1, 0)
    rec(0, 4)
    return ans[0]


def main():
    N, B = NMI()

    print(solve(N, B))

    # cnt = 0
    # while True:
    #     N = random.randint(1, 100000)
    #     B = random.randint(1, 100000)
    #     res_lazy = solve_lazy(N, B)
    #     res = solve(N, B)
    #
    #     if res_lazy != res or cnt >= 10000:
    #         print(N, B)
    #         print(res_lazy, res)
    #         break
    #
    #     cnt += 1


if __name__ == "__main__":
    main()
