n=int(input())
b=1
for i in range(1,n+1):
    b=b*i
print(b)

a=int(input())
l=[]
while a>0:
    l.append(a%10)
    a=a//10
print(l.count(0))

print('Решите уравнение 47x+13=154')
h=int(input())
while h!=3:
    print('Неверно')
    h=int(input())
print('Правильно')

p=int(input('Введите кол-во цифр: '))
print('Введите цифры')
r=p
j=[]
while p>1:
    v=int(input(''))
    j.append(v)
    p=p-1
for i in range(1,r+1):
    if i in j:
        j.remove(i)
    else:
        j.append(i)
print(int(j[0]))

laa=str(input('Введите числа：'))
pop=[]
while laa!='СТОП':
    pop.append(int(laa))
    laa=str(input())
y=sorted(pop, reverse=True)
print(y[0],y[1],y[2])

oo=int(input('Введите кол-во цифр '))
f1=1
f2=1
for i in range(oo):
    print(f1)
    f1,f2=f2,f1+f2

al=int(input())
bob=[]
while al>0:
    if (al%10)%2==0:
        bob.append(al%10)
    al=al//10
fr=sorted(bob,reverse=True)
if len(fr)>0:
    print(fr[0])
else:
    print('Четных чисел нет')