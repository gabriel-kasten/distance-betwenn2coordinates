dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))

total_segundos_dias = dias * 24 * 60 * 60
total_segundos_horas = horas * 60 * 60
total_segundos_minutos = minutos * 60

total_segundos = total_segundos_dias + \
    total_segundos_horas + total_segundos_minutos

print(f"{total_segundos} segundos.")
