import pandas as pd 



arquivo=pd.read_csv('bonus.txt',delimiter=';')  #Abrindo o arquivo sem ;
arquivo2=pd.read_csv('clientes.txt',delimiter=';')

arquivo=arquivo.sort_values(by='cliente')		#Ordenando o arquivo bonus a partir da coluna clientes
Novo=pd.merge(arquivo,arquivo2,on='cliente')	#Juntando os arquivos a partir da chave cliente
Novo['somasaldo']=Novo['saldo']+Novo['historico']
Novo.to_csv('DADOSPANDA.txt')					#criando e salvado no arquivo DADOSPANDA.txt