print('#1')
a=int(input())
b=[]
if a<0:
    print('Ошибка')
else:
    for i in range(a):
        b.append(i+1)
    print(b)
