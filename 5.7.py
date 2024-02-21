al=int(input())
bob=[]
while al>0:
    if (al%10)%2==0:
        bob.append(al%10)
    al=al//10
fr=sorted(bob,reverse=True)
if len(fr)>0:
    print(fr[0])
else:
    print('Четных чисел нет')
