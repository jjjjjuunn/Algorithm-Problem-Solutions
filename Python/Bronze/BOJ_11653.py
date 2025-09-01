# Bronze 1
# 소인수분해
# 정수 N이 주어졌을 때, 소인수분해 하시오

def division_func(N):
    temp = N
    factors = []
    i = 2
    while i <= temp:
        if temp % i == 0:
            factors.append(i)
            temp //= i
        else:
            i += 1

    return factors

N = int(input())

factors = division_func(N)

for factor in factors:
    print(factor)