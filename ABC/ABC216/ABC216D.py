import sys
import math
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    K = []
    B = []
    Col = defaultdict(set)
    for i in range(M):
        K.append(NI())
        balls = NLI()
        for b in balls:
            Col[b].add(i)
        B.append(deque(balls))

    # 現在の一番上をsetで保持
    # queの中身がある限り取り出し、その筒から新しい球を出す
    # 新しく出した色が既にあれば、その2本の筒の番号をqueにつっこむ
    tops = set()
    que = deque()

    for i in range(M):
        que.append(i)

    while que:
        #print(que, tops)
        #print(B)
        col = que.popleft()
        if not B[col]:
            #print(f"B[{col}] is empty")
            continue
        top = B[col].popleft()
        if top not in tops:
            #print(f"{top} is new")
            tops.add(top)
        else:

            cols = Col[top]
            cols.discard(col)
            new_col = cols.pop()
            #print(f"{top} is exist in {new_col}")
            tops.discard(top)
            que.append(col)
            que.append(new_col)

        #print(que)

    if tops:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
