print('#8')
a=str(input())
k=0
a=a.split()
for i in range(len(a)):
    if int(a[i])>50:
        k+=1
print(k)
