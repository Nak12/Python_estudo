'''
Programa que solicita que usuario escreva uma frase, pede
para o usuario digitar uma letra e faz uma busca dessa letra na
frase escrita mais quantidade de vezes de sua ocorrencia.
'''

phrase = input('Digite sua frase: ')
letter = input('Digite a letra da qual deseja saber seu index: ')

qtd = 0

for i, c in enumerate(phrase):
	if c == letter:
		qtd += 1
		print(f"letra '{c}' na posicao: {i}")

if qtd > 0 :
	print(f"Quantidade de ocorrencias: {qtd}")
else:
	print("Nao ha ocorrencias da letra solicitada.")

	