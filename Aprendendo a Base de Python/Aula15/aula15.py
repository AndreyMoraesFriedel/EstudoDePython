t_carros=("Gol", "Voyage", "Santana") #Tupla

#Gambiarra para modificar uma Tupla
l_carros = list(t_carros)
l_carros[2] = "Focus"
t_carros = tuple(l_carros)

for x in t_carros:
    print(x)