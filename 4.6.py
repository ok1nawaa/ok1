from math import sqrt
a1,a2,a3=map(float,input().split())
disc=a2**2-4*a1*a3
if disc>=0:
    print(((-a2)+sqrt(disc))/(2*a1))
    print(((-a2)-sqrt(disc))/(2*a1))
else:
    print('корней нет')
