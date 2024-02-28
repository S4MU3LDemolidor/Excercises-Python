def notas (num1, num2, num3, letra):
    if letra == 'a':
        return (num1+num2+num3)/3
    elif letra == 'p':
        return (num1*5+num2*3+num3*2)/10
    
numero1 = float(input('Digite a nota 1: '))
numero2 = float(input('Digite a nota 2: '))
numero3 = float(input('Digite a nota 3: '))
palavra = input('Digite uma letra (A para aritimetrica e P para ponderada): ')

print(notas(numero1, numero2, numero3, palavra))