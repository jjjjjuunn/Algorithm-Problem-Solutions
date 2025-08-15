# 진법 변환 2
# 10진수 -> B진수

N,B = map(int,input().split())

if N==0:        # N == 0 일 때의 경우까지 고려
    print(0)    

else:
    B_list = []

    while True:
        if N == 0:
            break
        B_list.append(N % B)
        N //= B
            
    result = []

    for i in range(len(B_list)-1,-1,-1):
        if B_list[i] >= 10:
            alpha = chr(B_list[i]+ord('A')-10)
            result.append(alpha)
        else :
            result.append(B_list[i])

    print(*result,sep='')
