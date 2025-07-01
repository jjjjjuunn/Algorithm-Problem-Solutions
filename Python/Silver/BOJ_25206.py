# 너의 평점은
# 다시 한 번 풀어보기

grade_dict = {
    'A+' : 4.5, 'A0' : 4.0,
    'B+' : 3.5, 'B0' : 3.0,
    'C+' : 2.5, 'C0' : 2.0,
    'D+' : 1.5, 'D0' : 1.0,
    'F' : 0.0 
}

total_time = 0 
total_score = 0

for _ in range(20):
    subject, time, grade = input().split()
    time = float(time)
    if grade == 'P':
        continue
    score = grade_dict[grade]
    total_time += time
    total_score += score * time

print(total_score / total_time)
