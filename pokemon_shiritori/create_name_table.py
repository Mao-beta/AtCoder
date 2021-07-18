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


def convert_name(name):
    name = name.strip("ー").replace("♂", "オス").replace("♀", "メス") \
            .replace("ャ", "ヤ").replace("ュ", "ユ").replace("ョ", "ヨ") \
            .replace("ァ", "ア").replace("ィ", "イ").replace("ゥ", "ウ") \
            .replace("ェ", "エ").replace("ォ", "オ") \
            .replace("2", "ツ").replace("Z", "ト")
    return name[0] + name[-1]


def main():
    df = pd.read_csv("./pokemon.csv")
    df["名前"] = df["名前"].apply(lambda x: x.split("(")[0].strip(" "))
    df = df[["全国ナンバー", "名前"]].copy()
    df = df.drop_duplicates().reset_index(drop=True)
    df.columns = ["number", "name"]
    df["name_c"] = df["name"].apply(convert_name)
    df.to_csv("./pokemon_names.csv", index=None)


if __name__ == "__main__":
    main()
