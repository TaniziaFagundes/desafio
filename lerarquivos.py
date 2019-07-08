from math import*
import re
import json
import pandas as pd
from functools import reduce

def magic(value):
    parts = re.split(r'(\d+)', value)
    return [int(part) if part.isdigit()  else part  for part in parts] #isdigit() retorna v ou f se é digito


arquivo=open('bonus.txt','r') 			#abrir arquivo para leitura
conteudo=arquivo.readlines()			# definiu a variavel para receber o conteudo do arquivo
arquivo.close() 						#fecha arquivo

arquivo2=open('clientes.txt','r')
conteudo2=arquivo2.readlines()
arquivo2.close()

aux=sorted(conteudo, key=lambda v: magic(v[0:2]))  #ordenando arquivo bonus mas não está inserindo em


"""

arq=open('DADOS.txt','r')
for linha in arq:
	linha=linha.rstrip()
	print(linha)
arq.close()
"""