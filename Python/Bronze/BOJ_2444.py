# 별 찍기 - 7

n = int(input())

# 위쪽 삼각형 (가운데 포함)
for i in range(1,n+1):
    print(' '*(n-i)+ '*'*(2*i-1))

# 아래쪽 삼각형 (가운데 제외)
for i in range(1,n):
    print(' '* i + '*'*(2*n-(2*i+1)))