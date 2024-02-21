print('#7')
b1=int(input())
n=[]
for i in range(b1):
    n.append(str(input()))
f1=str(input())
for i in range(b1):
    if n[i].find(f1):
        print(n[i])
