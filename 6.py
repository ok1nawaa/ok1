a=int(input())
while a<0:
    print('Введите положительное число!')
    a=int(input())
if a==0:
    print('Число не имеет делителей!')
for x in range(1,a+1):
    k=0
    for y in range(1,a+1):
        if x%y==0:
            k+=1
    print(x,'-',k)  

b=int(input())
l=1
j=0
while b<0:
    print('Введите положительное число!')
    b=int(input())
for x1 in range(1,b+1):
    for y1 in range(1,x1+1):
        l*=y1
    j+=l
    l=1
print(j)

s,d=map(int,input('Введите два числа: ').split())
h=0
for n in range(s,d+1):
    for m in range(1,n+1):
        if n%m==0:
            h+=1
    if h<=2:
        print(n)
    h=0




