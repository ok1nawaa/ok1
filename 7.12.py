print('#12')
a=str(input())
b=[]
a=a.split()
for i in range(len(a)):
    b.append(int(a[i]))
print(str(sorted(b)))
print(str(sorted(b, reverse=True)))
