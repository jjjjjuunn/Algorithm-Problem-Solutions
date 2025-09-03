# Bronze 2
# 소수찾기

N = int(input())
numbers = list(map(int,input().split()))

prime_number_list = []

for num in numbers:
    if num == 1 :
        continue
    else :
        factor_list = []
        for i in range(2,num):
            if num % i == 0:
                factor_list.append(i)

        if len(factor_list) == 0 :
            prime_number_list.append(num)
    
print(len(prime_number_list))
        
    