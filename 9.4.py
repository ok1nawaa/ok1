n=int(input())
mat=[[int(i) for i in input().split()] for a in range(n)]
f=[]
l=[]
for i in range(n):
    for j in range(n-1,-1,-1):
        print(mat[j][i], end=' ')
    print()
