A, B, C, D = map(int, input().split())
taka = (C+B-1)//B
aoki = (A+D-1)//D
print('Yes' if taka <= aoki else 'No')