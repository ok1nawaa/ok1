a=int(input())
l=[]
while a>0:
    l.append(a%10)
    a=a//10
print(l.count(0))
