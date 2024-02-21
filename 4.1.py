n=int(input())
e=0
if n>2:
    e=2*10.5+(n-2)*4
elif n>0 and n<=2:
    e=n*10.5
else:
    print('введите корректное кол-во лет')
print(e)
