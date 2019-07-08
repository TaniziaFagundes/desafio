import os
import sys
import pandas as pd
from functools import reduce

# variaveis globais
cod = ['id', 'tentrada', 'tservico', 'prioridade', 'tipo'] 
nome_do_arquivo = "a"      # nome do arquivo a ser lido
processos = []          # lista de todos os processos
lista = []

# le o arquivo de processos e os coloca em uma lista
def ler_arquivo(nome):

    # passa todas as linhas para uma lista
    arq = open(nome, "r") 
    texto = arq.readlines()
               
    arq.close()
    # cria uma lista de processos onde cada processo eh uma lista
    
    linhas_sem_espaco = [list(map(lambda x : x.strip(), linha.split(";"))) for linha in texto]
    linhas_to_int = [list(map(lambda x : int(x) if x.isdigit() == True else x, p)) for p in linhas_sem_espaco]
    
    return linhas_to_int

# imprime a lista
def imprimir(lista):
    for processo in lista:
        print (processo)

lista1 = ler_arquivo("bonus.txt")
lista2 = ler_arquivo("clientes.txt")

bonus = lista1.pop(0)
clientes = lista2.pop(0)

# lista1.sort(key=lambda x: x[0])
# lista2.sort(key=lambda x: x[0])

lista1 = sorted(lista1, key=lambda x: x[0])  
lista2 = sorted(lista2, key=lambda x: x[0])  



for x in range(len(lista1)):
    lista.insert(x, lista1[x])
    lista[x].extend(lista2[x][1:])
    lista[x].append(lista1[x][1]+lista1[x][2])

lista.sort(key=lambda x:x[1], reverse=True)

lista.insert(0, bonus)
lista[0].extend(clientes[1:])
lista[0].append('saldo_historico')

lista_str = [list(map(str, p)) for p in lista]
lista_str = [list(map(lambda x:"NaN" if x=="" else x,p))for p in lista_str]
arq=open('DADOS.csv','w') 

for p in lista_str:
    #p = ";".join(p)
    arq.writelines(p)
    arq.writelines("\n")
arq.close()
