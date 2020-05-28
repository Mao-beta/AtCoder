#入力
N = int(input())
x, y = map(int, input().split())
a = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for i in range(N):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
dp = [[] for _ in range(N)]