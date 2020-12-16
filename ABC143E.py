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


#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append((edge[1], edge[2]))
        res[edge[1]].append((edge[0], edge[2]))
    return res



def main():
    N, M, L = NMI()
    edges = [NLI() for _ in range(M)]
    adj = make_adjlist_nond(N, edges)
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    #print(adj)

    INF = 301
    # best_moves[s][t]はsからtまでの移動で最小回数、最大残燃料
    best_moves = [[[INF, 0] for _ in range(N+1)] for _ in range(N+1)]

    for start in range(1, N+1):
        queue = deque()
        queue.append((start, 0, L, 0))
        #print(start, "start")
        while queue:
            now, num, fuel, prev = queue.popleft()
            #print(now, num, fuel)

            for goto, need in adj[now]:
                if need > L or goto == prev:
                    continue
                best_num, best_fuel = best_moves[start][goto]
                #print(goto, "best", best_num, best_fuel)
                if fuel >= need:
                    if num < best_num or (num == best_num and fuel-need > best_fuel):
                        #print("case1")
                        queue.append((goto, num, fuel-need, now))
                        best_moves[start][goto] = [num, fuel-need]

                else:
                    if num+1 < best_num or (num+1 == best_num and L-need > best_fuel):
                        #print("case2")
                        queue.append((goto, num+1, L-need, now))
                        best_moves[start][goto] = [num+1, L-need]

    #print(best_moves)
    for s, t in querys:
        ans = best_moves[s][t][0]
        print(ans if ans != INF else -1)






if __name__ == "__main__":
    main()
