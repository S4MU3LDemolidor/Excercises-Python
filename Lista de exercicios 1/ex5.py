def idade (anos, meses, dias):
    anos_para_dias = anos*360
    meses_para_dias = meses*30
    dias_totais = anos_para_dias+meses_para_dias+dias
    return f'O usuario tem uma quantidade de dias vividos equivalente a {dias_totais}'

ano = int(input('Quantos anos: '))
mes = int(input('Quantos meses: '))
dia = int(input('Quantos dias: '))

print(idade(ano, mes, dia))
