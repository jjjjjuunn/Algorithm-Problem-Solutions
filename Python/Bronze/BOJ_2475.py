import math

a,b,c,d,e = map(int,input().split())

sum = pow(a,2)+pow(b,2)+pow(c,2)+pow(d,2)+pow(e,2)
valid_n = sum % 10

print(valid_n)