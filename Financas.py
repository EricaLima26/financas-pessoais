from opcao import mostrar_menu
from opcao import registrar
from opcao import ver_extratos

while True:
    escolha = mostrar_menu()
        
    if escolha == "1":
        registrar()
    elif escolha == "2":
        ver_extratos()

