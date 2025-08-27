# Bronze 1
# 달팽이는 올라가고 싶다
# 무조건 다시 풀어보기

A, B, V = map(int, input().split())

if V == A :
    days = 1
    print(days)
    
else:
    if (V - A) % (A - B) == 0 :
        days = (V - A) // (A - B) + 1
    else :
        days = (V - A) // (A - B) + 2

    print(days)