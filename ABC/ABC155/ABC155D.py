import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    A = NLI()
    A_pos = []
    A_neg = []
    for a in A:
        if a >= 0:
            A_pos.append(a)
        else:
            A_neg.append(a)
    A_pos.sort()
    A_neg.sort(reverse=True)
    n_pos = len(A_pos)
    n_neg = len(A_neg)

    def get_num(x):
        # Aのうち2個ペアの積でx以下のものの個数
        res = 0

        # pos[i]==a * pos[:r]の探索
        r = n_pos
        for i, a in enumerate(A_pos):
            while r >= 1 and A_pos[r-1] * a > x:
                r -= 1
            res += r

        # neg[i]==a * neg[:r]の探索
        r = n_neg
        for i, a in enumerate(A_neg):
            while r >= 1 and A_neg[r-1] * a > x:
                r -= 1
            res += r

        # 自分同士のペアを削除
        for i, a in enumerate(A):
            if a**2 <= x:
                res -= 1

        # ダブルカウントを削除
        res = res // 2

        # neg[i]==a * pos[l:]の探索
        l = n_pos
        for i, a in enumerate(A_neg):
            while l > 0 and A_pos[l-1] * a <= x:
                l -= 1
            res += n_pos - l

        return res

    # ok -> mid以下を満たす積がK個以上ある
    ok = 10**19
    ng = -10**19
    while abs(ok-ng) > 1:
        mid = (ok + ng) // 2
        num = get_num(mid)
        if num >= K:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()
