temperatura_celsius = 0
temperatura_farenheit = 0

temperatura_celsius = float(input('Digite a temperatura em celsius'))
if (temperatura_celsius >= -273.15):
    temperatura_farenheit = temperatura_celsius * 1.8 + 32
    print('A temperatura em farenheit é: ', temperatura_farenheit)
else:
    print('A temperatura digitada é menor que a temperatura mínima possível')