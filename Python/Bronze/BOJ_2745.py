# 진법 변환
# 다시 한 번 풀어보기

N, B = input().split()
B = int(B)

result = 0
power = 0

# 오른쪽부터 왼쪽까지 각 자릿수 처리
for i in range(len(N)-1,-1,-1):
    char = N[i]
    if char.isdigit():
        digit_value = int(char)
    else :
        digit_value = ord(char)-ord('A')+10
    
    result += digit_value * (B**power)
    power += 1

print(result)