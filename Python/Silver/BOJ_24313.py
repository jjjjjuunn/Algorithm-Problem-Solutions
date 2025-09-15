# Silver 5
# 알고리즘 수업 -점근적 표기 1

# 핵심 개념 : 기울기 비교

a1, a0 = map(int,input().split())
c = int(input())
n0 = int(input())

if a1 <= c:
    if a1 * n0 + a0 <= c * n0:
        print(1)
    else:
        print(0)

else:
    print(0)