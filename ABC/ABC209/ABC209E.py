import sys
import math
from collections import Counter
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
    N = NI()
    W = [SI() for _ in range(N)]

    use_w = set()
    for w in W:
        use_w.add(w[:3])
        use_w.add(w[-3:])

    zipped, unzipped = compress(use_w)

    V = len(zipped)
    E = [[] for _ in range(V)]
    RE = [[] for _ in range(V)]
    outs = [0] * V

    for w in W:
        _from = zipped[w[:3]]
        _to = zipped[w[-3:]]
        E[_from].append(_to)
        RE[_to].append(_from)
        outs[_from] += 1

    states = [-1] * V
    # -1: draw, 0: win, 1: lose

    que = deque()

    for node, out in enumerate(outs):
        if out == 0:
            states[node] = 1
            que.append(node)

    while que:
        now = que.popleft()

        for goto in RE[now]:
            if states[goto] != -1: continue

            outs[goto] -= 1
            if states[now] == 1:
                states[goto] = 0
                que.append(goto)

            elif outs[goto] == 0:
                states[goto] = 1
                que.append(goto)

    answer = {0: "Aoki", 1: "Takahashi", -1: "Draw"}
    for w in W:
        node = zipped[w[-3:]]
        state = states[node]
        print(answer[state])


if __name__ == "__main__":
    main()
