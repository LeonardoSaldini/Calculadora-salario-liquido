inss =  0
ir = 0

print(30*'-')
print('Calculador de salário liquído')
print(30*'-')

salario = float(input('Digite o valor do salário bruto: '))

if salario <= 1212.00:
    inss = salario * 0.075
if 1212.00 < salario <= 2427.15:
    inss = (salario * 0.09) - 18.18
if 2427.15 < salario <= 3641.03:
    inss = (salario * 0.12) - 91.00
if 3641.03 < salario <= 7087.22:
    inss = (salario * 0.14) - 163.82
if salario > 7087.22:
    inss = 828.38

num_dependentes = int(input('Número de dependentes: '))
if num_dependentes == 0:
    total_inss = salario - inss
else:
    total_inss = salario - inss - (num_dependentes * 189.59)


if 1903.88 < total_inss <= 2826.65:
    ir = (total_inss * 0.075) - 142.80
if 2826.65 < total_inss <= 3751.05:
    ir = (total_inss * 0.15) - 354,80
if 3751.05 < total_inss <= 4664.68:
    ir = (total_inss * 0.225) - 636.13
if total_inss > 4664.68:
    ir = (total_inss  * 0.275) - 869.36

salario_liq = salario - (inss + ir)

print(f'O valor do inss = {inss:.2f}\nO valor do IRRF = R${ir:.2f}\nSalário liquído é de R${salario_liq:.2f}')


