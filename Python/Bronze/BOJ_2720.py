# Bronze 3
# 세탁소 사장 동혁
test_case_num = int(input())

for _ in range(test_case_num):
    C = int(input())

    Q = C // 25
    C %= 25
    
    D = C // 10
    C %= 10

    N = C // 5
    C %= 5

    P = C

    print(Q, D, N, P)

# 간결한 버전
test_case_num = int(input())

for _ in range(test_case_num):
    C = int(input())

    coins = [25,10,5,1]
    result = []

    for coin in coins:
        result.append(C//coin)
        C %= coin
    
    print(*result)