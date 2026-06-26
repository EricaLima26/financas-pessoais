import opcao

print("=== MENU DE OPÇÕES ===")
print("1 - Registar")
print("2 - Ver extratos")
print("3 - Relatório")
print("4 - Exportar")
print("5 - Sair")

escolha = input("Digite o número da opção desejada: ")

if escolha == "1":
    opcao.registrar()
