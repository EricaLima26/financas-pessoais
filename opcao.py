import json
import os

ARQUIVO = "Lancamento.json"

def mostrar_menu():
    print("=== MENU DE OPÇÕES ===")
    print("1 - Registrar")
    print("2 - Ver extratos")
    print("3 - Relatório")
    print("4 - Exportar")
    print("5 - Sair")

    escolha = input("Digite o número da opção desejada: ")
    return escolha

def carregar_lancamentos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def salvar_lancamentos(lancamentos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lancamentos, f, indent=4, ensure_ascii=False)

def registrar():
    lancamentos = carregar_lancamentos()

    while True:
        print("\n=== REGISTRAR ===")
        data = input("Digite a data (dd/mm/aaaa): ").strip()
        tipo = input("Digite o tipo (receita/ despesa): ").strip().lower()
        if tipo not in ["receita", "despesa"]:
            print("Tipo inválido! Digite 'receita' ou 'despesa'.")
            continue
        break

    while True:
        try:
            valor = float(input("Digite o valor: ").replace(",", "."))
            if valor <= 0:
                raise ValueError("O valor deve ser positivo.")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}")

    categoria = input("Digite a categoria: ").strip()
    descricao = input("Digite a descrição: ").strip()

    registro = {
        "data": data,
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
    }

    lancamentos.append(registro)
    salvar_lancamentos(lancamentos)

    print("\nRegistro salvo com sucesso!")
    print()

def ver_extratos():
    lancamentos = carregar_lancamentos()

    if not lancamentos:
        print("📭 Nenhum lançamento encontrado.")
        return

    print("\n=== EXTRATO DE LANÇAMENTOS ===")
    for i, lanc in enumerate(lancamentos, start=1):
        data = lanc.get("data", "N/A")
        tipo = lanc.get("tipo", "N/A").capitalize()
        categoria = lanc.get("categoria", "N/A")
        descricao = lanc.get("descricao", "N/A")
        valor = lanc.get("valor", 0.0)

        print(f"{i}. {data} | {tipo} | {categoria} | {descricao} |  R$ {valor:,.2f}")
    print()



