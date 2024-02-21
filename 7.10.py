print('#10')
a=str(input())
a=a.split()
b=a.index(max(a, key=lambda i: int(i)))
c=a.index(min(a, key=lambda i: int(i)))
a[b],a[c]=a[c],a[b]
print(' '.join(a))
