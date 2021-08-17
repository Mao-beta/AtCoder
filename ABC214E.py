import sys
from heapq import heappop, heappush, heapify
from collections import defaultdict
import bisect

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
        N = NI()
        B = [NLI() for _ in range(N)]

        # 同じLでまとめる
        BD = defaultdict(list)
        for l, r in B:
            BD[l].append(r)

        # ありえるlのリスト、あとで二分探索する
        Ls = list(BD.keys())
        Ls.sort()
        L_idx = 0
        LN = len(Ls)

        # 箱に詰めてもよい球のrを管理
        R = []
        heapify(R)

        # 現在見ている箱の数字を10**9までシミュレート
        i = 0
        while i <= 10**9:
            # いま追加できる球がなく、入れられる球もないとき飛ばす
            # 飛ばす先は次に追加できるi
            if not BD[i] and not R:
                L_idx = bisect.bisect_left(Ls, i)
                if L_idx < LN:
                    i = Ls[L_idx]

            # いま見ている箱から入れてよくなる球をすべて手持ちに追加
            for r in BD[i]:
                heappush(R, r)

            # 手持ちの球があるならいま見ている箱にひとつ入れる
            if R:
                r = heappop(R)
                # 貪欲に詰めたのにあふれたので失敗
                # 詰めようとした球を手持ちに戻してbreak
                if i > r:
                    heappush(R, r)
                    break

            # もう追加できず、手持ちもないなら終了
            if L_idx == LN and not R:
                break

            i += 1

        # 全部終わってなお手持ちがあれば失敗
        if R:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
