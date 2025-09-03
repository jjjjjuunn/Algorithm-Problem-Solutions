# Bronze 4
# 삼각형 외우기
# 세 개의 각을 받아 삼각형의 종류 출력하기

angle_list = list(int(input()) for _ in range(3))

if sum(angle_list) != 180:
    print("Error")
elif angle_list.count(60) == 3:
    print("Equilateral")
    
# elif angle_list[0] == angle_list[1] or angle_list[1] == angle_list[2] or angle_list[0] == angle_list[2]:
#     print("Isosceles")

# 이등변 삼각형을 판별하는 다른 방법
elif len(set(angle_list)) == 2:
    print("Isosceles")
else:
    print("Scalene")
