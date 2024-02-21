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
