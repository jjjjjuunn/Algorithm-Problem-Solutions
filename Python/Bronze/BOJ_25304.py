price_total = int(input())
type_num = int(input())

price_cal = 0
for i in range(type_num):
    price,num = map(int,input().split())
    price_cal += price * num

if price_total == price_cal:
    print("Yes")
else :
    print("No")