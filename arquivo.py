import pandas as pd
from functools import reduce


bonus=pd.read_csv("clientes.txt", sep = ";")
clientes=pd.read_csv("bonus.txt", sep = ";")

with open("clientes.txt","w") as fim:
	clientes=pd.read_csv(clientes)
clientes.close()

with open("bonus.txt","w") as fim:
	bonus=pd.read_csv(bonus)
bonus.close()

print(bonus.head(11))
print(clientes.head(11))


reduce(lambda x, y: pd.merge(x, y, on = ["clientes"]), [bonus,clientes])  #um arquivo tem mais colunas que outro
#resultado=pd.concat([df.set_index(["clientes"]) for df in [bonus,clientes]]).reset_index()

dados=open("DADOS.txt",'w')
arq=dados.wrilelines(resultado)
print(arq)

"""
resultado = [pd.read_csv("clientes.txt"), pd.read_csv("bonus.txt")]
resultado = pd.concat(resultado)
print(resultado.head(11)) #linhas a exibir==10

with open ("bonus.txt", "r") as fim:
    dados = pd.read_csv(fim, delimiter=";")
    print(dados)
    lista = list(dados)
    lista_ordenada = sorted (lista, key = lambda dado: int(dado[1]))

    for x in lista_ordenada:
      print(x)

"""