print('#2')
from random import *
c=[]
for i in range(10):
    c.append(randint(1,100))
print(c)
c[2]=randint(1,100)
print(c)
