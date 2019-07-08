import os
import sys


cod = ['id', 'tentrada', 'tservico', 'prioridade', 'tipo']    # variaveis globais
nome_do_arquivo = "a"      # nome do arquivo a ser lido
processos = []          # lista de todos os processos
lista = []

# le o arquivo de processos e os coloca em uma lista
def ler_arquivo(nome): 		

    arq = open(nome, "r") 	# passa todas as linhas para uma lista
    texto = arq.readlines()
               
    arq.close()
    # cria uma lista de processos onde cada processo eh uma lista
    linhas_sem_espaco = [map(lambda x : x.strip(), linha.split(";")) for linha in texto]
    linhas_to_int = [map(lambda x : int(x) if x.isdigit() == True else x, p) for p in linhas_sem_espaco]
    
    return linhas_to_int


def imprimir(lista):  # imprime a lista
    for processo in lista:
        print(processo)

lista1 = ler_arquivo("bonus.txt")
lista2 = ler_arquivo("clientes.txt")

lista1.sort(key=lambda x: x[0])
lista2.sort(key=lambda x: x[0])

bonus = lista1.pop()
clientes = lista2.pop()

for x in range(len(lista1)):
    lista.insert(x, lista1[x])
    lista[x].extend(lista2[x][1:])

lista.insert(0, bonus)
lista[0].extend(clientes[1:])

lista_str = [map(str, p) for p in lista]
arq=open('DADOS.txt','w') 

for p in lista_str:
    p = ";".join(p)
    arq.writelines(p)
arq.close()