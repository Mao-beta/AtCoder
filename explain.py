import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N, M = NMI()
    F = [NLI() for _ in range(M)]
    tree = make_adjlist_nond(N, F)

    ans = 0
    seen = [0] * (N + 1)
    for start in range(1, N+1):
        que = deque()
        que.append(start)

        seen[start] = 1
        fri_cnt = 1
        while que:
            now = que.popleft()

            for goto in tree[now]:
                if seen[goto]:
                    continue
                seen[goto] = 1
                fri_cnt += 1
                que.append(goto)
        ans = max(fri_cnt, ans)
    print(ans)





if __name__ == "__main__":
    main()