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
