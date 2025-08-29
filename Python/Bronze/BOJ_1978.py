# Bronze 2
# 소수 찾기
# 주어진 숫자 N개 중에서 소수가 몇 개인지 찾는 문제
# 입력 처리하는 거 처음에 헤맸음.
'''
N = int(input())
numbers = list(map(int,input().split()))

prime_number_list = []

for num in numbers:
    if num == 1 :
        continue
    else :
        factor_list = []
        for i in range(2,int(num**0.5)+1):  # 개선: 제곱근까지만 확인
            if num % i == 0:
                factor_list.append(i)

        if len(factor_list) == 0 :
            prime_number_list.append(num)
    
print(len(prime_number_list))
'''

# 함수 버전
N = int(input())
numbers = list(map(int, input().split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_count = 0
for num in numbers:
    if is_prime(num):
        prime_count += 1

print(prime_count)
        
    