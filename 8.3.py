print('#3')
a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b=0
a=a[0]+a[1]+a[2]
for i in range(len(a)):
    b=int(a[i])+b
print(b/len(a))
