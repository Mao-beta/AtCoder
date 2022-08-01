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


class KindDeque():
    """
    D = KindDeque()
    D.kindで種類数を、len(D)で長さを、
    D.Cで中身のkeyごとの個数（要はCounterのような辞書）を
    O(1)で取ってこれるdeque
    """
    def __init__(self):
        self.D = deque()
        self._k = 0
        self.C = defaultdict(int)

    @property
    def kind(self):
        return self._k

    def __len__(self):
        return len(self.D)

    def append(self, x):
        self.D.append(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def appendleft(self, x):
        self.D.appendleft(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def pop(self):
        x = self.D.pop()
        self.C[x] -= 1
        if self.C[x] == 0:
            self._k -= 1

    def popleft(self):
        x = self.D.popleft()
        self.C[x] -= 1
        if self.C[x] == 0:
            self._k -= 1


def main():
    N, K = NMI()
    A = NLI()

    que = KindDeque()
    ans = 0

    for i, a in enumerate(A):
        que.append(a)

        while que.kind > K:
            que.popleft()

        ans = max(ans, len(que))

    print(ans)


if __name__ == "__main__":
    main()
