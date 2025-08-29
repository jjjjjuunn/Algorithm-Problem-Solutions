# Bronze 1
# 약수들의 합
# 숫자 n이 완전수인지 판단하기
# 출력시 join() 활용법 익히기
 
while True :
    n = int(input())
    if n == -1:
        exit(0)

    factor_list = []

    for i in range(1,n):
        if n % i == 0:
            factor_list.append(i)

    factor_sum = sum(factor_list)
    if factor_sum == n:
        result = ' + '.join(map(str,factor_list))
        print(f"{n} = {result}")
    else :
        print(f"{n} is NOT perfect.")