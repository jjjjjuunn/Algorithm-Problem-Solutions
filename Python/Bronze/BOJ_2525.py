#오븐 시계
# 다시 한 번 풀어보기
H,M = map(int,input().split())
x = int(input())

total = x + 60*H + M

H = (total//60) % 24
M = total % 60

print(H,M)