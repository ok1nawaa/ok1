b=int(input())
l=1
j=0
while b<0:
    print('Введите положительное число!')
    b=int(input())
if b==1 or b==0:
    print('1')
else:
    for x1 in range(1,b+1):
        for y1 in range(1,x1+1):
            l*=y1
        j+=l
        l=1
    print(j)
