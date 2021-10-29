a = [1,2,3,4,5,6,7,2]
b = [3,4,5,6,7,8,3,2]
c = []

for i in range(1, len(a)):
    if(a[i] != b[i]):
       c.append(i)
print(c)
