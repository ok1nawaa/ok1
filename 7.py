print('#1')
a=int(input())
b=[]
if a<0:
    print('Ошибка')
else:
    for i in range(a):
        b.append(i+1)
    print(b)

print('#2')
from random import *
c=[]
for i in range(10):
    c.append(randint(1,100))
print(c)
c[2]=randint(1,100)
print(c)

print('#3')
d=[]
for i in range(26):
    d.append(str(chr(97+i))*(i+1))
print(d)

print('#4')
a1=int(input())
f1=[]
f2=[]
for i in range(a1):
    f1.append(list(input()))
a2=int(input())
for i in range(a1):
    f2.append(f1[i][a2-1])
print(''.join(f2))

print('#5')
aa=int(input())
aaa=[]
for i in range(aa):
    aaa.extend(list(input()))
print(aaa)

print('#6')
b1=int(input())
n=[]
for i in range(b1):
    n.append(str(input()))
for i in n:
    while n.count(i)>1:
        n.remove(i)
for i in range(len(n)):
    print(n[i])

print('#7')
b1=int(input())
n=[]
for i in range(b1):
    n.append(str(input()))
f1=str(input())
for i in range(b1):
    if n[i].find(f1):
        print(n[i])

print('#8')
a=str(input())
k=0
a=a.split()
for i in range(len(a)):
    if int(a[i])>50:
        k+=1
print(k)

print('#9')
a=str(input())
b=str(input())
print(b.join(a))

print('#10')
a=str(input())
a=a.split()
b=a.index(max(a, key=lambda i: int(i)))
c=a.index(min(a, key=lambda i: int(i)))
a[b],a[c]=a[c],a[b]
print(' '.join(a))

print('#11')
a=str(input())
a=a.split()
b=a.index(max(a, key=len))
c=a.index(min(a, key=len))
a[b],a[c]=a[c],a[b]
print(' '.join(a))

print('#12')
a=str(input())
b=[]
a=a.split()
for i in range(len(a)):
    b.append(int(a[i]))
print(str(sorted(b)))
print(str(sorted(b, reverse=True)))

print('#13')
a=str(input()).split()
print(*[int(a[i])**2 for i in range(len(a)) if int(a[i])%2==0 and int(a[i])**2%10!=4])
      



