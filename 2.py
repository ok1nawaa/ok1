a=int(input())
print(a-3,a-2,a-1,a,a+1,a+2,a+3,sep=",")
b=int(input())
c=int(input())
print('',b,"+",c,"=",b+c,'\n',b,"-",c,"=",b-c,'\n',b,"*",c,"=",b*c,'\n',b,"/",c,"=",b/c,'\n',b,"//",c,"=",b//c,'\n',b,"%",c,"=",b%c,'\n',b,"**",c,"=",b**c)
d=int(input())
e=int(input())
print('Кол-во мандаринов на школьника =',e//d)
print('Осталось мандаринов =',e%d)
f=int(input())
g=[]
g.append(f//100)
g.append(f%100//10)
g.append(f%10)
print(g[0],g[1],g[2],sep='')
print(g[0],g[2],g[1],sep='')
print(g[1],g[0],g[2],sep='')
print(g[1],g[2],g[0],sep='')
print(g[2],g[0],g[1],sep='')
print(g[2],g[1],g[0],sep='')
h=int(input())
if h<0:
    h*=-1
j=[]
for i in range(4):
    j.append(h%10)
    h//=10
print('',j[3],'\n',j[2],'\n',j[1],'\n',j[0])