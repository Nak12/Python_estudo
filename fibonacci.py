'''
Programa simples que gera os numeros de Fibonacci como valor 
limite pelo usuario.
'''

qtd = int(input('Digite o valor limite gerado por Fibonacci: '))

if qtd > 1:
	a, b = 0, 1

	while b < qtd:
		print(b, end = " ")
		a, b = b, a+b
else:
	print("Erro! Digite um numero maior ou igual a 2.")

print()