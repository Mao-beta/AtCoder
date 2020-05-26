N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
tour = [1]
gone = [0] * (N+1)

for i in range(N):
    now = tour[-1]
    if gone[now]:
        save = now
        break
    gone[now] = 1
    tour.append(A[now])

save_idx = tour.index(save)

if K <= save_idx:
    print(tour[K])
    exit()

loop = tour[save_idx+1:]
K = K - save_idx - 1
print(loop[K % len(loop)])
