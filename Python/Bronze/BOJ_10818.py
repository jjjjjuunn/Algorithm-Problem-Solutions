# 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

n = int(input())
arr = list(map(int,input().split()))

#더 파이썬스러운 버전
print(min(arr),max(arr))

#반복문으로 구현
'''
max_val = min_val = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_val :
        max_val = arr[i]
    if min_val>arr[i] :
        min_val = arr[i]

print(min,max)
'''