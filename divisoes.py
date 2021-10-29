listar = [1,2,3,4,5,6,7,8,9,10,20,30,40]

for i in listar:
    if(i % 3 == 0):
        print("para")
    if(i % 5 == 0):
        print("peba")
    if(i % 3 == 0 and i % 5 == 0):
        print("parapeba")
    else: 
        print(i)
