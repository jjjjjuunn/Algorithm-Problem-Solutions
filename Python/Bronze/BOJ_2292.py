# Bronze 2
# 벌집

boundary_num = 1
hexagon_num = 0
boundary_producing_num = 2

# 바운더리 하나를 형성하기 위해서는 6의 배수가 필요함 6->12->18->24->30-> ....
# 바운더리가 언제 증가하느냐? 2->8->20->38->62
N = int(input())

while N > 1+3*boundary_num*(boundary_num-1):
    boundary_num += 1

'''
while hexagon_num != N:
    hexagon_num+=1
    if hexagon_num == boundary_producing_num :
        boundary_num+=1
        boundary_producing_num += 6 * (boundary_num-1)
'''
print(boundary_num)


# 방법 3
n = int(input())
end = 1
count = 1
while n > end:
    end += 6 * count
    count += 1
print(count)