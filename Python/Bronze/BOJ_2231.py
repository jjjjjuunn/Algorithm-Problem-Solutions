# 분해합
# Bronze 2
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

N = int(input())

for num in range(1,N):
    each_total = N - num
    temp = list(str(num))
    each_list = []

    for each in temp:
        each_list.append(int(each))

    if each_total == sum((each_list)):
        print(num)
        exit(0)

print(0)
    
