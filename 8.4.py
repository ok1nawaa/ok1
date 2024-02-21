print('#4')
n=int(input())
a=[]
if n<=0:
    print('Ошибка')
else:
    for i in range(n):
        a.append(i+1)
    for i in range(n):
        print(a)
