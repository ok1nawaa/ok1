print('#1')
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']
list1[2][1][2].extend(sub_list)
print(list1)

print('#2')
a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(a)
a[0]=list(reversed(a[0]))
a[1]=list(reversed(a[1]))
a[2]=list(reversed(a[2]))
print(a)

print('#3')
a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b=0
a=a[0]+a[1]+a[2]
for i in range(len(a)):
    b=int(a[i])+b
print(b/len(a))

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

print('#5')
a=input().split()
b=[]
for i in range(len(a)):
    if i>0 and a[i]==a[i-1]:
        b[len(b)-1].append(a[i])
    else:
        b.append([a[i]])   
print(b)