def valor (num):
    if num % 2 == 0:
        return f'O numero {num} e par!'
    else:
        return f'O numero {num} e impar!'

numero = int(input('Digite um valor inteiro: '))
print(valor(numero))
