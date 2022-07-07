sexo = int(input('Digite 1 para Homem ou 2 para Mulher: '))
if sexo == 1:
        altura = float(input('Digite sua altura: '))
        print((72.7 * altura) - 58)
else:
    if sexo == 2:
        altura = float(input('Digite sua altura: '))
        print((62.1 * altura) - 44.7)
    else:
        print('Opção errada tente novamente!')