# 최댓값
# 기존 ver
'''
arr = []
for i in range(9):
    arr.append(int(input()))
'''
#리스트 컴프리헨션
# _는 변수를 사용하지 않는다는 뜻의 관례적 표현
arr = [int(input())for _ in range(9)]

max_val = max(arr)
print(max_val)
print(arr.index(max_val) + 1)