print('#11')
a=str(input())
a=a.split()
b=a.index(max(a, key=len))
c=a.index(min(a, key=len))
a[b],a[c]=a[c],a[b]
print(' '.join(a))
