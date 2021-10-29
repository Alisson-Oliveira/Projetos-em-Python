valor = float(input(""))

notaDois = 0
notaCinco = 0
notaDez = 0
notaVinte = 0
notaCinquenta = 0
notaCem = 0
rest = valor
def calculo(rest, valor, dividir):
   nota =  (valor - rest)/dividir
   return nota


while(rest > 2):
   if(valor >= 100):
      rest = valor %  100
      notaCem = calculo(rest, valor, 100)
      valor = rest
   if(rest >=50):
      rest = valor %  50
      print(rest)
      notaCinquenta = calculo(rest,valor, 50)
      valor = rest
   if(rest >= 20):
      rest = valor %  20
      notaVinte = calculo(rest, valor, 20)
      valor = rest
   if(rest >=10):
      rest = valor %  10
      notaDez = calculo(rest, valor, 10)
      valor = rest
   if(rest >=5):
      rest = valor %  5
      notaCinco = calculo(rest, valor, 5)
      valor = rest
   if(rest >= 2):
      rest = valor %  2
      notaDois = calculo(rest, valor, 2)
      valor = rest
   else: 
      rest = 1



print("Notacem", notaCem)
print("nota Cinquenta",notaCinquenta)
print("nota vinte",notaVinte)
print("nota dez",notaDez)
print("nota cinco",notaCinco)
print("nota dois",notaDois)
