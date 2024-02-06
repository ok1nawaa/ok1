a=input('Введите пароль:')
b=input('Введите пароль еще раз:')
if a==b:
    print('Успешно')
else:
    print('Ошибка')
c=int(input())
if c%2==0:
    print('Четное')
else:
    print('Нечетное')
d,e,f,g=map(int,input().split())
h=[d,e,f,g]
print(min(h))
k=0
for i in range(3):
    j=int(input())
    if j>0:
        k+=j
print(k)
l=int(input())
if l>=1000 and l<10000 and (l%7==0 or l%17==0):
    print('Красивое')
else:
    print('Страшное')
v,x,y,z=map(int,input().split())
if x+y+v+z>=4 and x+y+z+v<=36:
    if v==y or x==z:
        if v==y and x==z:
            print('фигура и так на этой клетке')
        else:
            print('да')
    else:
        print('нет')
else:
        print('нет')

