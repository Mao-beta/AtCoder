import sys
import math
from collections import deque
from itertools import permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    S = [SI() for _ in range(3)]

    # 最上位と末位
    S_first = [s[0] for s in S]
    S_last = [s[-1] for s in S]

    # 使いうる文字
    use_chrs = set("".join(S))
    # 文字の種類数
    n_chrs = len(use_chrs)

    # 10種類より多ければ解けない
    if n_chrs > 10:
        print("UNSOLVABLE")
        exit()

    # 辞書の初期化
    EtoN = {s: 0 for s in use_chrs}

    # 辞書を元に文字から数字に変換する関数
    def calc(T, dic):
        T = T[::-1]
        res = 0
        for i, t in enumerate(T):
            res += dic[t] * 10**i
        return res

    # 10_P_nの順列　※listにはしない
    Perm = permutations(range(10), n_chrs)

    for case in Perm:
        # 今回の辞書
        for s, n in zip(use_chrs, case):
            EtoN[s] = n

        # 一の位の数字
        A0 = EtoN[S_last[0]]
        B0 = EtoN[S_last[1]]
        C0 = EtoN[S_last[2]]

        # 一の位の和が違うなら無理
        if (A0 + B0) % 10 != C0:
            continue

        # 最上位が0はダメ
        if 0 in {EtoN[S_first[0]], EtoN[S_first[1]], EtoN[S_first[2]]}:
            continue

        A = calc(S[0], EtoN)
        B = calc(S[1], EtoN)
        C = calc(S[2], EtoN)

        if A + B == C:
            print(A, B, C, sep="\n")
            exit()

    print("UNSOLVABLE")


if __name__ == "__main__":
    main()
