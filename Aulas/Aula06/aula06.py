curso="Curso de Python"; #String Array de Caracteres

#print(curso[9:15]); #Mostrar de onde começar e onde parar
#print(curso.strip()); #remove espaço no começo e no fim da String
#print(curso.lower().strip()); #Deixar em minusculo + Strip
#print(curso.upper().strip()); #Deixar em MAIUSCULO + Strip
#print(curso.replace("Python","C#")); #Replace para troca de String/Caractere

a=curso.split(" ") #Divisao e retorno em Array

print(a[2])
print("Tamanho: " + str(len(curso)));