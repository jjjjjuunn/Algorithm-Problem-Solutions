# Bronze 3
# 약수 구하기

# 간단한 버전
'''
N, K = map(int, input().split())

factor_list = []

for i in range(1,N+1):
    if N % i == 0:
        factor_list.append(i)
    
if len(factor_list) >= K :
    print(factor_list[K-1])
else :
    print(0)
'''
# 메모리 최적화 버전
N, K = map(int, input().split())

count = 0
for i in range(1,N+1):
    if N % i == 0 :
        count += 1
        if count == K :
            print(i)
            exit(0)

print(0)