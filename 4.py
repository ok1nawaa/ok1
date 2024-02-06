n=int(input())
e=0
if n>2:
    e=2*10.5+(n-2)*4
elif n>0 and n<=2:
    e=n*10.5
else:
    print('введите корректное кол-во лет')
print(e)

b,c,d=map(int,input().split())
a=[b,c,d]
f=sorted(a)
print('',f[2],'\n',f[1],'\n',f[0])

aa=int(input())
bb=[aa//100,aa//10%10,aa%10]
cc=sorted(bb)
if cc[2]-cc[0]==cc[1]:
    print('Прикольное')
else:
    print('не прикольное')

g,h,j=map(str,input().split())
k=[g,h,j]
l=sorted(k,key=len)
print('',l[0],'\n',l[2])

hh=str(input())
if '@' and '.' in hh:
    print('да')
else:
    print('нет')

from math import sqrt
a1,a2,a3=map(float,input().split())
disc=a2**2-4*a1*a3
if disc>=0:
    print(((-a2)+sqrt(disc))/(2*a1))
    print(((-a2)-sqrt(disc))/(2*a1))
else:
    print('корней нет')