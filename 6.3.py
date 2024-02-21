s,d=map(int,input('Введите два числа: ').split())
h=0
for n in range(s,d+1):
    for m in range(1,n+1):
        if n%m==0:
            h+=1
    if h<=2:
        print(n)
    h=0
