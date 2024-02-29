#Criação da Matriz
carros=[
    ["Modelo", "HRV"],
    ["Fabricante", "Honda"],
    ["Ano", 2016]
]

##Inserindo uma nova colecão dentro da Matriz
carros.append(["Cor", "Prata"]) 

#Alterando Elemento
carros[2][1] = 2019 

#Mostrando Elemento específico
print(f"{carros[1][0]}\n") 

#Mostrando cada elemento da Matrizes
for l in carros: 
    for c in l:
        print(f"{c}")



