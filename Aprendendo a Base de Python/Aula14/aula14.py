#limpar a tela

###carros=["gol","parati","voyage","saveiro","bora"]
#=i=0
#tam = len(carros)
#while i < tam:
#    print(carros[i])
#    i+=1
###print("Fim do Programa!")

import os
os.system('cls')
carros = []

carro = input("Digite nome do carro: ")
while carro != "-1":
    carros.append(carro)
    carro = input("Digite nome do carro: ")

os.system('cls')

for x in carros:
    print(x)