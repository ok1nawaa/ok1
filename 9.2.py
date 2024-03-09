row, col=int(input()), int(input())
matrix=[list(map(int, input().split())) for a in range(row)]
i=int(input())
j=int(input())
for b in matrix:
    b[i],b[j]=b[j],b[i]
    print(*b)