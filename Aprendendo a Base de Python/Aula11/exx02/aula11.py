clima="chuv"
dinheiro = 299
lugar=""

if clima=="sol" or (dinheiro>=300 and dinheiro<=500):
    lugar = "clube"
elif clima=="chuva" and dinheiro<300:
    lugar = "Shopping"
else:
    lugar = "Cinema"

print("Vou ao " + lugar)