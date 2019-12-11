#coding:utf-8
import random

def tamanhoString(palavra):
    """ está função verifica o tamanho de umma string.
    :param palavra: recebe uma string
    :return: um inteiro
    """
    contador = 0
    for caracter in palavra:
        contador = contador + 1

    return contador


def compararValores(valor1, valor2):
    """ está função compara dois valores.
    :param valor1: recebe string ou inteiro
    :param valor2: recebe string ou inteiro
    :return: True, se a condição for aceita
    """
    if valor1 == valor2:
        return True
    else:
        return False


def transformarEmLista(palavra):
    """ está função transforma uma string em uma lista.
    :param palavra: uma string
    :return: uma lista
    """
    lista = []
    for caracter in palavra:
        lista.append(caracter)
    return lista


def palavrasPadrao():
    """ está função escolhe aleatoriamente uma palavra.
    :return: uma string
    """
    palavrasFrutas = random.randint(1, 6)

    if palavrasFrutas == 1:
        return "abacaxi"
    elif palavrasFrutas == 2:
        return "manga"
    elif palavrasFrutas == 3:
        return "melancia"
    elif palavrasFrutas == 4:
        return "banana"
    elif palavrasFrutas == 5:
        return "abacate"
    elif palavrasFrutas == 6:
        return "morango"


def escolherPalavra():
    """ está função pergunta ao usúario qual modo de jogo
    ele deseja.
    :return: uma string
    """
    print (organizarCodigo(1))
    print ("     MODO DE JOGAR     ")
    print (organizarCodigo(1))
    print (" - 1 - Individual")
    print (" - 2 - Multiplayer")
    print (organizarCodigo(1))

    opcao = int(input("Digite sua opção: "))
    print (organizarCodigo(1))
    if opcao == 1:
        palavraUsuarioIndividual = palavrasPadrao()
        return palavraUsuarioIndividual
    else:
        palavraUsuarioMultiplayer = input("Digite sua palavra: ")
        return palavraUsuarioMultiplayer


def escolherDica():
    """ está função pergunta ao usúario qual a dica será utilizada.
    :return: uma string
    """
    print (" - 1 - Digitar dica")
    print (" - 0 - Dica padrão(Caso tenha escolhido INDIVIDUAL)")
    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        dicaUsuario = input("Digite sua palavra: ")
        return dicaUsuario
    else:
        dicaPadrao = " F R U T A "
        return dicaPadrao


def organizarCodigo(tipo):
    """ está função organizar o jogo com asteriscos " * ".
    :param tipo: recebe um inteiro
    :return: uma string
    """
    if tipo == 1:
        return "-" * 25

    if tipo == 2:
        return "-" * 30

    if tipo == 3:
        return "-" * 35

    if tipo == 4:
        return "-" * 40


def verificarCaracter(caracter1, caracter2):
    """ está função verifica se duas strings ou duas listas
    possuem o mesmo caracter.
    :param caracter1: recebe um caracter
    :param caracter2: recebe uma string ou uma lista
    :return: True, se a condição for aceita
    """
    if caracter1 in caracter2:
        return True
    else:
        return False


def construirPalavra(tentativa, palavra, palavraVisualizada, palavraOculta):
    """ está função verifica se existe uma letra
    em uma palavra.
    :param tentativa: recebe um caracter
    :param palavra: recebe uma string
    :param palavraVisualizada: recebe uma lista com o nome da palavra escolhida
    :param palavraOculta: recebe uma lista com a palavra oculta
    :return: letras que existem na palavra
    """
    if tentativa == palavra:
        return palavraVisualizada

    for controle in range(0, tamanhoString(palavra)):
        if tentativa in palavraVisualizada:
            if palavraVisualizada[controle] == tentativa:
                palavraOculta[controle] = palavraVisualizada[controle]

    return palavraOculta