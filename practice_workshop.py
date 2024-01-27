# rho = 7800 # плотность железа
# r_fe = 0.1 # удельная проводимость железа
# s = float(input('Введите площадь поперечного сечения в мм2: '))
# u = float(input('Введите напряжение в цепи: '))
# I = float(input('Введите силу тока в цепи: '))

# print(u * s / (r_fe * I) * s / 10**6 * rho, 'кг')

heater_ressistance = float((input('Введите сопротивление нагревателя: ')))
reo_ressistance = float(input('Введите сопротивление реостата: '))
R0 = heater_ressistance + reo_ressistance # общее сопротивление последовательныых элементов
U = float((input('Введите напряжение: ')))
I0 = U / R0
print(I0**2*reo_ressistance)
