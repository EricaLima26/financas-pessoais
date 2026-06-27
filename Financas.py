from opcao import mostrar_menu
from opcao import registrar
from opcao import relatorio
from opcao import ver_extratos
from opcao import exportar

while True:
    escolha = mostrar_menu()
        
    if escolha == "1":
        registrar()
    elif escolha == "2":
        ver_extratos()
    elif escolha == "3":
        relatorio()
    elif escolha == "4":
        exportar()
    else:
        print("Saindo do programa")
        break
        
        