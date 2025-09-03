# Bronze 2
# 소수

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