a = [1,2,3,4,4]
b = [4,3,4,5,6]
c = []

def mergeList(list):
   for i in list:
       c.append(i)

mergeList(a)
mergeList(b)

print(sorted(c))
