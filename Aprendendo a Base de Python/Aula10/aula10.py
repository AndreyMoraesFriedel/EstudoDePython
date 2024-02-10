a = 10
b = 5
res=0
open="/"

if open=="+":
    res = a + b
if open=="-":
    res = a - b
if open=="/":
    res = a / b
if open=="*":
    res = a * b

print(f"{a} {open} {b} = {res}")
print("Fim Do Programa")