# Bronze 2
# 소수
# 자연수 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 구해라
# 초기 구현 때 엣지케이스(1,2) 처리에 문제가 있었음

'''
M = int(input())
N = int(input())

prime_num_list = []

for i in range(M,N+1):
    if i == 1:
        continue
    elif i == 2:
        prime_num_list.append(i)
        continue
    
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i-1:
            prime_num_list.append(i)

if sum(prime_num_list) == 0:
    print(-1)
else:
    print(sum(prime_num_list))
    print(prime_num_list[0])
'''

# 함수로 구현
# 단일 책임 원칙: 한 함수는 하나의 일만 -> 함수 쪼개보기
'''
def find_primes_in_range(M,N):
    
    prime_num_list = []

    for num in range(M, N+1):
        if num == 1:
            continue
        if num == 2:
            prime_num_list.append(num)
            continue

        for factor in range(2, num):
            if num % factor == 0:
                break
            if factor == num - 1:
                prime_num_list.append(num)

    return prime_num_list

M = int(input())
N = int(input())

primes = find_primes_in_range(M,N)
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
'''
# 함수 쪼깨서 구현한 최종 버전
def is_prime_single(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1): # 범위를 제곱근까지로 제한하여 최적화
        if  num % i == 0:
            return False
    return True

def find_primes_in_range(M: int,N: int):
    primes = []
    for num in range(M, N+1):
        if is_prime_single(num):
            primes.append(num)
    return primes

M = int(input())
N = int(input())

primes = find_primes_in_range(M,N)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))