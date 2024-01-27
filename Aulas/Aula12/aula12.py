#Utilizando For para ler uma List
carros=["parati",
        "voyage",
        "gol",
        "santana"]

for x in carros:
    print(x)
    if(x=="gol"):
        break

print("Fim Do Programa!")

#DICA: podemos combinar o for com o metodo range e assim podemos fazer por exemplo a tabuada de todos os numero de 1 a 10, segue o codigo:

for y in range(1,11):
    for x in range(1,11):
        print(f"{y} x {x} = {y*x}")
    print("\n")