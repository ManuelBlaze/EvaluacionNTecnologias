'''
Manuel Alejandro Escobar Mira - Grupo 2
'''

nombre = str(input('Ingrese su nombre \n'))
salario = float(input('Ingrese su salario \n'))
he = int(input('Ingrese las horas extra trabajadas \n'))
hd = int(input('Ingrese las horas dominicales trabajadas \n'))

vDia = (salario/30)
vHora = (salario/240)
vHoraE = vHora * 1.35
vHoraD = vHora * 1.75

tHE = vHoraE * he
tHD = vHoraD * hd

total = (salario + tHE + tHD)

print(f'Empleado: {nombre}')
print(f'Salario: $ {int(salario)}')
print(f'Valor del día: $ {int(vDia)}')
print(f'Valor de la hora: $ {int(vHora)}')
print(f'Horas Extras: {he}')
print(f'Valor hora Extra: $ {int(vHoraE)}')
print(f'Total x Hora Extra: $ {int(tHE)}')
print(f'Horas Dominicales: {hd}')
print(f'Valor hora Dominical: $ {int(vHoraD)}')
print(f'Total x Hora Dominical: $ {int(tHD)}')
print(f'Total a pagar: $ {int(total)}')

if total < 1000000:
    print(f'{nombre} solicita aumento.')
elif total < 2000000:
    reten = total * 0.02
    total -= reten
    print(f'{nombre}, su salario - retencion es de $ {int(total)} y la retencion es del 2% = $ {int(reten)}')
elif total <= 3000000:
    reten = total * 0.03
    total -= reten
    print(f'{nombre}, su salario - retencion es de $ {int(total)} y la retencion es del 3% = $ {int(reten)}')
else:
    reten = total * 0.04
    total -= reten
    print(f'{nombre}, su salario - retencion es de $ {int(total)} y la retencion es del 4% = $ {int(reten)}')
