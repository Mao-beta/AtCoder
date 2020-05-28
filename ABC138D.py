from _collections import deque
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

points = [0]*(N+1)
for i in range(Q):
    p, x = map(int, input().split())
    points[p] += x

stack = deque()
stack.append(1)
score = 0
score_array = [0]*(N+1)
is_checked = [0]*(N+1)
#print(graph)
while stack:
    node = stack.pop()
    is_checked[node] = 1

    #print("node=" + str(node))
    score_array[node] += points[node]
    #print("score=" + str(score_array[node]))
    for goto in graph[node]:
        if not is_checked[goto]:
            #print("goto=" + str(goto))
            stack.append(goto)
            score_array[goto] += score_array[node]

print(" ".join(map(str, score_array[1:])))

