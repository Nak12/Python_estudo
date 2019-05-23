'''
Programa simples imprime uma matriz criada pelo usuário.
'''

def cria_matriz(linhas, colunas):
	matriz = []
	for i in range(linhas):
		linha = []
		for j in range(colunas):
			valor = int(input("Digite o elemento ["+str(i)+"]["+str(j)+"]"))
			linha.append(valor)
		matriz.append(linha)
	return matriz 

def le_matriz():
	lin = int(input("Digite o numero de linhas da matriz: "))
	col = int(input("Digite o numero de colunas da matriz: "))
	return cria_matriz(lin, col)

def imprime(m):
	for i in m:
		for j in i:
			print(j, end = ' ')
		print()

if __name__ == '__main__':
	myMatrix = le_matriz()
	imprime(myMatrix)