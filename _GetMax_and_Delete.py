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


from heapq import heappop, heappush
from collections import defaultdict

class GetMax_and_Delete:
    """
    最大値取得と要素削除を高速で行えるデータ構造
    同じkeyは許容しない
    """
    def __init__(self):
        self.neg = []
        self.out = []
        # dic: key -> valの変換用の辞書
        # 削除と同時にNoneになる
        self.dic = defaultdict(lambda: None)

    def exist(self, key):
        if self.dic[key] is None:
            return False
        else:
            return True

    def add(self, val, key):
        """
        val, keyの要素を追加
        すでに存在するkeyの場合は無視
        """
        if self.exist(key):
            return

        heappush(self.neg, (-val, key))
        self.dic[key] = val

    def _del(self, key):
        del self.dic[key]

    def delete(self, key):
        """
        keyの要素を削除候補outに突っ込む
        dicからは消しておく
        存在しないkeyを消そうとした場合はValueError
        """
        if not self.exist(key):
            raise ValueError("The key you wanna delete does not exist")

        val = self.dic[key]
        heappush(self.out, (-val, key))
        self._del(key)

    def get_max(self):
        """
        valが最大の要素に関して(val, key)を取得する
        空集合の場合は(None, None)を返す
        """
        while self.neg and self.out:
            if self.neg[0][1] == self.out[0][1]:
                heappop(self.neg)
                heappop(self.out)
            else:
                break

        if not self.neg:
            return None, None

        val, key = self.neg[0][0] * (-1), self.neg[0][1]
        return val, key


def main():
    pass


if __name__ == "__main__":
    main()
