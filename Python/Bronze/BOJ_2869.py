# Bronze 1
# 달팽이는 올라가고 싶다

A, B, V = map(int, input().split())

Day = 0

if A - B == 1 :
    Day = V - A + 1

else :
    Hight = A
    while True :
        Hight += (A-B)
        Day+=1
        if V < Hight :
            break

print(Day)
