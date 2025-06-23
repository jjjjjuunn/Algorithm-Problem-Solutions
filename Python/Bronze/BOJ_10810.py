# 공 넣기
# print(*arr)로 한 줄에 공백 구분 출력이 가능하다
# arr = [0] * N처럼 리스트를 곱해서 원하는 크기만큼 초기화하는 방식은 파이썬에서만 가능한 문법
N,M = map(int,input().split())

arr = [0] * N   
for _ in range(M):
    i,j,k = map(int,input().split())
    for idx in range(i-1,j):
        arr[idx] = k

print(*arr)
