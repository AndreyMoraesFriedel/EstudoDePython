a = 10
b = 5
res=0
open="$"

if open=="+":
    res = a + b
elif open=="-":
    res = a - b
elif open=="/":
    res = a / b
elif open=="*":
    res = a * b
else:
    print("Error[Operador]")

print(f"{a} {open} {b} = {res}")
print("Fim Do Programa")