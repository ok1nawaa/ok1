n=int(input())
for i in range(n):
    for j in range(n):
        if i==j or i==n-1-j:
            print('1'.ljust(2), end=' ')
        else:
            print('0'.ljust(2), end=' ')
    print()