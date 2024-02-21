print('#13')
a=str(input()).split()
print(*[int(a[i])**2 for i in range(len(a)) if int(a[i])%2==0 and int(a[i])**2%10!=4])
