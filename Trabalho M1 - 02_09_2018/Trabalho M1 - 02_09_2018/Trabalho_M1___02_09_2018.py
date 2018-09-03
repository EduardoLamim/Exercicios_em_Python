def solicitarNumeros(quantidade):
    for listaNumeros in range(quantidade):
        lista.append(int(input("Digite um número: ")))

    return lista

def exercicio03():

    solicitarNumeros(10)
    
    print ("\nNúmeros pares da lista:\n")

    for item in lista:
        if item % 2 == 0:
            print (item)

    print ("\n")

#-----------------------------------------------------------------------------------------------

def exercicio04():

    solicitarNumeros(10)

    posicaoMaior = 0
    posicaoMenor = 0
    somaDosNumerosImpares = 0

    comparacao = lista[0]
    menorValor = lista[0]
    maiorValor = lista[0]

    for valor in lista:
        if valor > comparacao:
            maiorValor = valor
            posicaoMaior = lista.index(valor)
            comparacao = valor

    comparacao = lista[0]

    for valor in lista:
        if valor < comparacao:
            menorValor = valor
            posicaoMenor = lista.index(valor)
            comparacao = valor

        if valor % 2 == 1:
            somaDosNumerosImpares = somaDosNumerosImpares + 1
            
    print ("\nMaior valor: " + str(maiorValor))
    print ("Posição do maior valor no array: " + str(posicaoMaior))
    print ("\nMenor valor: " + str(menorValor))
    print ("Posição do menor valor no array: " + str(posicaoMenor))
    print ("\nSoma dos números ímpares: " + str(somaDosNumerosImpares))

    print ("\n")

#---------------------------------------------------------------------------------------------

def exercicio05():

    print ("Primeiro aluno:\n")

    aluno1 = { 
                "nome": input("Digite o nome do aluno: "), 
                "curso": input("Digite o curso: "), 
                "nota1": input("Digite a primeira nota: "),
                "nota2": input("Digite a segunda nota: "),
                "nota3": input("Digite a terceira nota: ")
             }


    os.system('cls' if os.name == 'nt' else 'clear')

    print ("Segundo aluno:\n")

    aluno2 = { 
                "nome": input("Digite o nome do aluno: "), 
                "curso": input("Digite o curso: "), 
                "nota1": input("Digite a primeira nota: "),
                "nota2": input("Digite a segunda nota: "),
                "nota3": input("Digite a terceira nota: ")
             }

    os.system('cls' if os.name == 'nt' else 'clear')

    print ("Terceiro aluno:\n")

    aluno3 = { 
                "nome": input("Digite o nome do aluno: "), 
                "curso": input("Digite o curso: "), 
                "nota1": input("Digite a primeira nota: "),
                "nota2": input("Digite a segunda nota: "),
                "nota3": input("Digite a terceira nota: ")
             }

    os.system('cls' if os.name == 'nt' else 'clear')

    print ("Quarto aluno:\n")

    aluno4 = { 
                "nome": input("Digite o nome do aluno: "), 
                "curso": input("Digite o curso: "), 
                "nota1": input("Digite a primeira nota: "),
                "nota2": input("Digite a segunda nota: "),
                "nota3": input("Digite a terceira nota: ")
             }

    os.system('cls' if os.name == 'nt' else 'clear')

    print ("Quinto aluno:\n")

    aluno5 = { 
                "nome": input("Digite o nome do aluno: "), 
                "curso": input("Digite o curso: "), 
                "nota1": input("Digite a primeira nota: "),
                "nota2": input("Digite a segunda nota: "),
                "nota3": input("Digite a terceira nota: ")
             }

    os.system('cls' if os.name == 'nt' else 'clear')

    mediaAluno1 = (int(aluno1["nota1"]) + int(aluno1["nota2"]) + int(aluno1["nota3"])) / 3 
    mediaAluno2 = (int(aluno2["nota1"]) + int(aluno2["nota2"]) + int(aluno2["nota3"])) / 3
    mediaAluno3 = (int(aluno3["nota1"]) + int(aluno3["nota2"]) + int(aluno3["nota3"])) / 3
    mediaAluno4 = (int(aluno4["nota1"]) + int(aluno4["nota2"]) + int(aluno4["nota3"])) / 3
    mediaAluno5 = (int(aluno5["nota1"]) + int(aluno5["nota2"]) + int(aluno5["nota3"])) / 3

    print("Os alunos aprovados foram:\n")
    
    if mediaAluno1 >= 6:
        print("Aluno: " + aluno1["nome"])
        print("Curso: " + aluno1["curso"])
        print("Aprovado com média: " + str(mediaAluno1) + "\n")

    if mediaAluno2 >= 6:
        print("Aluno: " + aluno2["nome"])
        print("Curso: " + aluno2["curso"])
        print("Aprovado com média: " + str(mediaAluno2) + "\n")

    if mediaAluno3 >= 6:
        print("Aluno: " + aluno3["nome"])
        print("Curso: " + aluno3["curso"])
        print("Aprovado com média: " + str(mediaAluno3) + "\n")

    if mediaAluno4 >= 6:
        print("Aluno: " + aluno4["nome"])
        print("Curso: " + aluno4["curso"])
        print("Aprovado com média: " + str(mediaAluno4) + "\n")

    if mediaAluno5 >= 6:
        print("Aluno: " + aluno5["nome"])
        print("Curso: " + aluno5["curso"])
        print("Aprovado com média: " + str(mediaAluno5) + "\n")

#--------------------------------------------- Início do programa ---------------------------------------------

import os

lista = []

print("Exercício 3 \n") 
exercicio03()

print("Exercício 4 \n")
exercicio04()

print ("Exercício 5 \n")
exercicio05()

