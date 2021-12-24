from tkinter import messagebox
# Sistema de loja simples sem interface

print("=-=-=-=-=-Sistema de loja Simples-=-=-=-=-=")
print()
print("             Menu de opções")
print()
print("1 - Produtos Masculinos")
print("2 - Produtos Femininos")
print("3 - Produtos Infantis")
print("4 - Produtos Variados")
print()
opcao = int(input("Escolha uma opção:"))
print()

# Variaveis que serao usadas
carrinhoCompras = [0]
produtos = [["calca"], ["blusa"], ["sapato"], ["short"]]
precos   = [[30], [25], [35], [10]]

# Opcao 1 Produtos Masculinos
if opcao == 1:

    print("Produtos masculinos disponiveis:")
    print("1 - Calças  - R$ 30,00")
    print("2 - Blusas  - R$ 25,00")
    print("3 - Sapatos - R$ 35,00")
    print("4 - Shorts  - R$ 10,00")
    
    continuar = 1
    while continuar != 0:
    
        carrinho = int(input("Qual produto deseja adicionar ao carrinho de compras:"))
        
        if carrinho == 1:
            carrinhoCompras.append(precos[0])
        elif carrinho == 2:
            carrinhoCompras.append(precos[1])
        elif carrinho == 3:
            carrinhoCompras.append(precos[2])
        elif carrinho == 4:
            carrinhoCompras.append(precos[3])
        else:
            print("Opcao invalida!")
        print("")
        continuar = int(input("0 Para sair. 1 Para continuar:"))
        print("")
    
    print("Carrinho de compras:", carrinhoCompras)
    
# Opcao 2 Produtos Femininos
elif opcao == 2:
    print("Produtos femininos disponiveis:")
    print("1 - Calças   - R$ 60,00")
    print("2 - Blusas   - R$ 30,00")
    print("3 - Sapatos  - R$ 35,00")
    print("4 - Shorts   - R$ 15,00")
    print("5 - Vestidos - R$ 12,00")
    
    continuar = 1
    while continuar != 0:
    
        carrinho = int(input("Qual produto deseja adicionar ao carrinho de compras:"))
        
        if carrinho == 1:
            carrinhoCompras.append(precos[0])
        elif carrinho == 2:
            carrinhoCompras.append(precos[1])
        elif carrinho == 3:
            carrinhoCompras.append(precos[2])
        elif carrinho == 4:
            carrinhoCompras.append(precos[3])
        else:
            print("Opcao invalida!")
        print("")
        continuar = int(input("0 Para sair. 1 Para continuar:"))
        print("")
    
    print("Carrinho de compras:", carrinhoCompras)
    
# Opcao 3 Produtos Infantis
elif opcao == 3:
    print("Produtos infantis disponiveis:")
    print("1 - Calças  - R$ 20,00")
    print("2 - Blusas  - R$ 15,00")
    print("3 - Sapatos - R$ 30,00")
    print("4 - Shorts  - R$ 8,00")
    
    continuar = 1
    while continuar != 0:
    
        carrinho = int(input("Qual produto deseja adicionar ao carrinho de compras:"))
        
        if carrinho == 1:
            carrinhoCompras.append(precos[0])
        elif carrinho == 2:
            carrinhoCompras.append(precos[1])
        elif carrinho == 3:
            carrinhoCompras.append(precos[2])
        elif carrinho == 4:
            carrinhoCompras.append(precos[3])
        else:
            print("Opcao invalida!")
        print("")
        continuar = int(input("0 Para sair. 1 Para continuar:"))
        print("")
    
    print("Carrinho de compras:", carrinhoCompras)
    
# Opcao 4 Produtos Variados
elif opcao == 4:
    print("Produtos variados disponiveis:")
    print("1 - Vestidos  - R$ 30,00")
    print("2 - Blusas    - R$ 25,00")
    print("3 - Sapatos   - R$ 35,00")
    print("4 - Shorts    - R$ 10,00")
    
    continuar = 1
    while continuar != 0:
    
        carrinho = int(input("Qual produto deseja adicionar ao carrinho de compras:"))
        
        if carrinho == 1:
            carrinhoCompras.append(precos[0])
        elif carrinho == 2:
            carrinhoCompras.append(precos[1])
        elif carrinho == 3:
            carrinhoCompras.append(precos[2])
        elif carrinho == 4:
            carrinhoCompras.append(precos[3])
        else:
            print("Opcao invalida!")
        print("")
        continuar = int(input("0 Para sair. 1 Para continuar:"))
        print("")
    
    print("Total Carrinho de compras:", carrinhoCompras)

else:
    print("Opcao invalida!")
    
soma = 0
for i in carrinhoCompras:
    soma = soma + i

print("Total carrinho compras:", (carrinhoCompras))    

arquivo = open("Recibo.txt", "a") # Cria o arquivo.txt caso nao exista, e escreve.
arquivo.write("\n--------------------------------------------------------------------------------\n\n")
arquivo.writelines("Escrito com sucesso!")
arquivo.write("--------------------------------------------------------------------------------")
arquivo.close()
messagebox.showinfo("Info", "Salvo com sucesso")
