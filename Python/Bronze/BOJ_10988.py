# 팰린드롬인지 확인하기

# 방법 1
ori_str = list(input())

new_str = list(reversed(ori_str))

for o,n in zip(ori_str,new_str):
    if o==n:
        continue
    else :
        print('0')
        exit(0)
        
print('1')

# 방법 2
'''
ori_str = input()

rev_str = ori_str[::-1]

print(1 if ori_str == rev_str else 0)
'''
'''
# 방법 2-1 : 더 간결한 버전
s = input()
print(1 if s == s[::-1] else 0)
'''