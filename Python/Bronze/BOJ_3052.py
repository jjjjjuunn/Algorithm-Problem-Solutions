# 나머지

# 방법 1: set(집합) 활용 - 서로 다른 나머지의 개수를 바로 구할 수 있음
num_set = {int(input()) % 42 for _ in range(10)}
print(len(num_set))

# 방법 2: set을 사용하지 않는 방식 (체크 배열)
# check[i]가 1이면 i라는 나머지가 등장했다는 의미
check = [0] * 42  # 나머지는 0~41, 총 42개
for _ in range(10):
    n = int(input())
    check[n % 42] = 1

# 방법 2-1: for문으로 1의 개수 세기
sum_val = 0
for i in range(42):
    sum_val += check[i]
print(sum_val)

# 방법 2-2: 파이썬 내장 sum() 함수로 더 간단하게
# print(sum(check))