# Bronze 2
# 블랙잭
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# 기존 내 코드
N, M  = map(int, input().split())

card_list = list(map(int, input().split()))
sum_set = set()

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum = card_list[i] + card_list[j] + card_list[k]
            
            if sum < M:
                sum_set.add(sum)

            elif sum == M:
                print(sum)
                exit(0)

sum_list = list(sum_set)
sum_list.append(M)
sum_list.sort()

print(sum_list[sum_list.index(M) - 1])

# 더 효율적인 방법
N, M  = map(int, input().split())

card_list = list(map(int, input().split()))

max_sum = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = card_list[i] + card_list[j] + card_list[k]
            
            if total <= M:
                max_sum = max(max_sum, total)

print(max_sum)

