n,m =[int(i) for i in input().split()]
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        if (i+j)%2==0:
            a[i].append('0')
        else:
            a[i].append('1')
for row in a:
    print(' '.join(row))