
print('#5')
a=input().split()
b=[]
for i in range(len(a)):
    if i>0 and a[i]==a[i-1]:
        b[len(b)-1].append(a[i])
    else:
        b.append([a[i]])   
print(b)
