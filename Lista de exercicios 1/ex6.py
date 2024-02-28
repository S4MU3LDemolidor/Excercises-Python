def numeros (num1, num2, num3):
    lista_numeros = [num1, num2, num3]
    lista_ordenada = sorted(lista_numeros)
    str(lista_ordenada)
    return f'Os numeros apresentados em ordem crescente e: {lista_ordenada}'

numero1 = int(input('Digite o primeiro numero (inteiro): '))
numero2 = int(input('Digite o segundo numero (inteiro): '))
numero3 = int(input('Digite o terceiro numero (inteiro): '))

print(numeros(numero1, numero2, numero3))
