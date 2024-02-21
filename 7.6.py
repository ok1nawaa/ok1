print('#6')
b1=int(input())
n=[]
for i in range(b1):
    n.append(str(input()))
for i in n:
    while n.count(i)>1:
        n.remove(i)
for i in range(len(n)):
    print(n[i])
