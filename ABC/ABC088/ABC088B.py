N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
if N == 1:
  print(A[0])
  exit()
print(sum(A[0::2]) - sum(A[1::2]))