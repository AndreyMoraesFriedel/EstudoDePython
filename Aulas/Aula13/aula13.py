from datetime import date

nomeUsuario = input("Digite nome do Usuario: ")
nascUsuario = int(input("Em que ano nasceu: "))

data_atual = date.today().year

idadeUsuario = data_atual - nascUsuario

print(f"""
    Usuario: {nomeUsuario}
    Idade: {idadeUsuario}
      """)
