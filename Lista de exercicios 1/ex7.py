def horas (segundos):

    #Obter tanto o quociente quanto o resto em uma única chamada de função
    
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)

    return f'{horas}:{minutos}:{segundos}'

seg = int(input('Digite uma hora em segundos: '))
print(horas(seg))
