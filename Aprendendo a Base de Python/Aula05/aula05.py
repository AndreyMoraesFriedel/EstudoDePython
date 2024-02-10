import random;

num_i=10;
num_f=8.5;
num_c=1j

#num_r=random.randrange(0,59);
num_r=[ #List Array
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59)
    ]
#Or num_r = [random.randrange(0, 59) for _ in range(6)]

x=num_r

for i in num_r:
    print(str(i))

print("Valor: " + str(x) + " - Tipo: " + str(type(x)));