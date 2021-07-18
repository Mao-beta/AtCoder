import sys
import pandas as pd
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def compress(S):
    """ 座標圧縮 """
    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    df = pd.read_csv("./pokemon_names.csv")
    N = len(df)

    # 使用されうるカタカナを座標圧縮してintに変換
    use_chars = set()
    for name in df["name_c"]:
        use_chars.add(name[0])
        use_chars.add(name[-1])
    zipped, unzipped = compress(use_chars)

    # 特定のカタカナで始まるもの、終わるものの辞書
    first_dic = {c: [] for c in zipped.keys()}
    last_dic = {c: [] for c in zipped.keys()}

    for i, name in enumerate(df["name_c"]):
        first_dic[name[0]].append(i)
        last_dic[name[-1]].append(i)

    # 遷移を示す隣接リストEと、その逆RE
    # degreesは出次数
    E = [[] for _ in range(N)]
    RE = [[] for _ in range(N)]
    degrees = [0] * N
    for i, name in enumerate(df["name_c"]):
        E[i] = first_dic[name[-1]][:]
        RE[i] = last_dic[name[0]][:]
        degrees[i] = len(E[i])
        #print(df["name"][i], degrees[i], E[i])

    # 後退解析
    # statesが-1->未定、0->負け、1->勝ち
    states = [-1] * N
    que = deque()

    # 出次数0のノードは負け、queに入れる
    for i, deg in enumerate(degrees):
        if deg == 0:
            states[i] = 0
            que.append(i)

    # 探索
    while que:
        now = que.popleft()

        for goto in RE[now]:
            # すでに勝敗が決まっていればとばす
            if states[goto] != -1:
                continue

            # 出次数を1減らす
            degrees[goto] -= 1

            # 自己ループはとばす
            if now == goto:
                continue

            # 現在必敗ならその前は必勝
            if states[now] == 0:
                states[goto] = 1
                que.append(goto)

            # 遷移のいずれも必敗でないならその前は必敗
            elif degrees[goto] == 0:
                states[goto] = 0
                que.append(goto)

    print(states)

    df["win"] = states

    df.to_csv("result.csv", index=None, encoding="shift-jis")


if __name__ == "__main__":
    main()
