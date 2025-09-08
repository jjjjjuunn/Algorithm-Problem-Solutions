# Bronze 3
# 삼각형과 세 변

while True: 
    side1, side2, side3 = map(int, input().split())

    if side1 == 0 and side2 == 0 and side3 == 0:
        break

    length_list = [side1, side2, side3]
    if max(length_list) >= (sum(length_list) - max(length_list)):
        print("Invalid")
    elif len(set(length_list)) == 1:
        print("Equilateral")
    elif len(set(length_list)) == 2:
        print("Isosceles")
    else:
        print("Scalene")

    
