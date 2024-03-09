n, m=map(int, input().split())
matrix=[]
a=1
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(a)
        a=a+1
        print(str(matrix[i][j]).ljust(2), end=' ')
    print()