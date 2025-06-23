#공 바꾸기
N,M = map(int,input().split())

arr = [num for num in range(1,N+1)]

for _ in range(M):
    i,j = map(int,input().split())
    arr[i-1],arr[j-1] = arr[j-1],arr[i-1]

print(*arr)