# 숫자의 합 구하기 (BOJ 11720)
# 입력: n(자리수), x(숫자)
# 출력: 각 자리수의 합

# 방법 1: 문자열 인덱싱 (언어에 상관없이 안전하게 쓸 수 있는 풀이)
n = int(input())
x = input()  # 숫자를 문자열로 입력받음
sum_val = 0
for i in range(n):
    sum_val += int(x[i])
print(sum_val)

# 파이썬다운 한 줄 풀이 (문자열 인덱싱 + map + sum)
# 각 문자를 int로 변환해 모두 더함
print(sum(map(int, x)))

# 방법 2: 정수 연산 (파이썬에서는 안전, C/C++ 등에서는 오버플로우 주의)
# x를 정수로 입력받아, 각 자리수를 나머지 연산(%)로 추출해 더함
# 단, 입력 숫자가 매우 클 경우 C/C++/Java에서는 오버플로우가 발생할 수 있음
n = int(input())
x = int(input())
sum_val = 0
for _ in range(n):
    sum_val += x % 10
    x //= 10
print(sum_val)

# 정리:
# - 문자열 인덱싱 방식은 언어에 상관없이 안전하게 쓸 수 있음
# - 정수 연산 방식은 파이썬에서는 안전하지만, C/C++/Java 등에서는 입력값이 크면 오버플로우가 발생할 수 있으니 주의!