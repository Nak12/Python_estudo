def cria_matriz(num_linhas, num_colunas, valor):
  matriz = []
  for i in range(num_linhas):
    #cria linhas i
    linha = []
    for j in range(num_colunas):
      #cria colunas j
      linha.append(valor)
    matriz.append(linha)
  return matriz

def soma_matriz(A, B):
  if mesmoTamanho(A, B):
    num_lin = len(A)
    num_col = len(A[0])
    C = cria_matriz(num_lin, num_col, 0)
    for linha in range(num_lin):
      for coluna in range(num_col):
        C[linha][coluna] = A[linha][coluna] + B[linha][coluna]
    return C
  print("As matrizes devem ter o mesmo tamanho.")

#Verifica se as duas matrizes possuem o mesmo tamanho
def mesmoTamanho(matrizA, matrizB):
  a = contaElem(matrizA)
  b = contaElem(matrizB)
  if a == b:
    return True
  return False

#Conta a quantidade de elementos de uma matriz
def contaElem(matriz):
  cont = 0
  for i in matriz:
    for j in i:
      cont += 1
  return cont

def main():
  #teste
  A = [[1,2,3], [4,5,6], [7,8,9]]
  B = [[10,20,30], [40,50,60], [70,80,90]]
  print(soma_matriz(A,B))

  C = [[1,2,3],[4,5]]
  D = [[10,20,30]]
  print(soma_matriz(C,D))

if __name__ == "__main__":
  main()
