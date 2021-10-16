#coding:utf-8
import Control

ask_again = True # Variaveis de controle
start_game = True

while start_game: # Manter o jogo rodando enquanto a condição for atendida

    palavra_escolhida = Control.escolherPalavra()

    palavra_dica = Control.escolherDica()

    palavra_lista = Control.transformarEmLista(palavra_escolhida)

    palavra_oculta = []
    for letras_ocultas in palavra_escolhida:
        palavra_oculta.append("_")

    print(Control.organizarCodigo(1))

    tentativas = []

    chances = 6

    erros = 0

    print ("\n")
    print ("VOCE TEM 6 CHANCES PARA ACERTAR A PALAVRA.")
    print ("\n")
    print ("A PALAVRA TEM", Control.tamanhoString(palavra_lista), "LETRAS")
    print ("\n")
    print ("A DICA É: ", palavra_dica)
    print ("\n")

    while ask_again:

        letra_palavra = input("DIGITE UMA LETRA (OU A PALAVRA): ")

        contruir_palavra = Control.construirPalavra(    letra_palavra,
                                                        palavra_escolhida,
                                                        palavra_lista,
                                                        palavra_oculta)

        print (Control.organizarCodigo(4))
        print ("PALAVRA: ", contruir_palavra)

        if Control.compararValores(contruir_palavra, palavra_lista):
            print ("\n")
            print ("YOU WIN")
            print (Control.organizarCodigo(4))
            break

        else:
            print (Control.organizarCodigo(4))

        if Control.compararValores(letra_palavra, palavra_escolhida):
            print ("\n")
            print ("YOU WIN")
            print (Control.organizarCodigo(3))
            break

        elif letra_palavra not in palavra_lista:

            if Control.verificarCaracter(letra_palavra, tentativas):
                print ("\n")
                print ("Você já tentou essa letra(ou palavra)")
                print ("\n")
                print ("LETRAS USADAS: ", tentativas)
                print ("\n")
                continue

            else:
                print ("\n")
                print ("Não há essa letra(ou palavra)")
                print ("\n")
                tentativas.append(letra_palavra)
                erros = erros + 1

                if Control.compararValores(erros, chances):
                    print ("VOCÊ ERROU", erros, "VEZES")
                    print ("\n")
                    ultimaTentativa = input("Ultima tentativa, digite uma Palavra: ")

                    if Control.compararValores(ultimaTentativa, palavra_escolhida):
                        print ("\n")
                        print ("YOU WIN")
                        print (Control.organizarCodigo(3))
                        break

                    else:
                        print ("\n")
                        print ("YOU LOSE")
                        print ("\n")
                        print ("A PALAVRA CORRETA ERA:", palavra_escolhida)
                        print (Control.organizarCodigo(3))
                        break

                else:
                    print ("LETRAS USADAS: ", tentativas)
                    print ("\n")
                    print ("ERROS: ", erros)
                    print ("\n")
                    continue

        else:

            if Control.verificarCaracter(letra_palavra, tentativas):
                print ("\n")
                print ("Você já tentou essa letra(ou palavra)")
                print ("\n")
                print ("LETRAS USADAS: ", tentativas)
                print ("\n")
                continue

            else:
                print ("\n")
                print ("Você acertou uma letra")
                tentativas.append(letra_palavra)
                print ("\n")
                print ("LETRAS USADAS: ", tentativas)
                print ("\n")
                continue

    break
