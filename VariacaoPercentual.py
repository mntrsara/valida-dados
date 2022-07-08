#validar os dados inseridos pelo usuario
while True:
    ValIni = input("Digite o valor inicial: ")
    ValIni = int(ValIni)
    if ValIni > 0:
        break

print()

#solicitando ao usuario o valor final
while True:
    ValFin = input("Digite o valor final: ")
    ValFin = int(ValFin)
    if ValFin >= 0:
        break

print()

#entrada de dados
DifVal = ValFin - ValIni
Perc = (abs(DifVal) / ValIni) * 100

if DifVal < 0:
    print("A variação percentual foi de -", Perc,"%")
else:
    print("A variação percentual foi de +", Perc,"%")