import sys
import os
import shutil
import math
from collections import deque


def main():
    contest = input("コンテスト名を入力：")
    file_num = input("作成ファイル数（F問題までなら6）：")
    num_to_ALP = {i: chr(i + 97).upper() for i in range(26)}

    if contest[0:3] in ["ABC", "ARC", "AGC"]:
        genre = contest[0:3]
        os.chdir(genre)
        if not os.path.exists(contest):
            os.mkdir(contest)
        os.chdir(contest)






if __name__ == "__main__":
    main()