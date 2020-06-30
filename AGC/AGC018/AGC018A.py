from math import gcd
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
gcm = 10**9+7
for i in range(N-1):
    gcm = min(gcm, gcd(A[i], A[i+1]))
if N == 1:
    print('IMPOSSIBLE' if K != A[0] else 'POSSIBLE')
    exit()

print('POSSIBLE' if K % gcm == 0 and K <= A[0] else 'IMPOSSIBLE')