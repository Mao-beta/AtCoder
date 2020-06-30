import bisect
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
A.sort()
B.sort()
C.sort()
BoverA = [0] * N
CoverB = [0] * N
for i in range(N):
    BoverA[i] = N - bisect.bisect_right(B, A[i])
    CoverB[i] = N - bisect.bisect_right(C, B[i])
cumBC = [0] * N
cumBC[N-1] = CoverB[N-1]
for i in range(N-2, -1, -1):
    cumBC[i] = cumBC[i+1] + CoverB[i]
ans = 0
for i in range(N):
    if N - BoverA[i] >= 0 and N - BoverA[i] < N:
        ans += cumBC[N - BoverA[i]]
print(ans)