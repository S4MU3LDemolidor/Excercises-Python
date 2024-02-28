def leNumero (num):
    if num > 0:
        print(f'O numero: {num} e um valor postivo')
    if num < 0:
        print(f'O numero: {num} e um valor negativo')

numero = int(input('Digite um valor inteiro: '))
leNumero(numero)
