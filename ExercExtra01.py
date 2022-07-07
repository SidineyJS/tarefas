valorunit = float(input('Valor Unitárioa R$: '))
qtde = int(input('Quantidade: '))
desconto = 1

if qtde >=10 and qtde <= 99:
    desconto = 0.95
elif qtde >= 100 and qtde <= 999:
    desconto = 0.90
elif qtde >=1000:
    desconto = 0.85
total_desconto = valorunit * desconto * qtde
total = valorunit * qtde
descontototal = total - total_desconto
print(f'Total sem desconto: R$ {total:.2f}')
print(f'Desconto: R$ - {descontototal:.2f}')
print(f'Total COM desconto: R$ {total_desconto:.2f}')