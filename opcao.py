import json
import os

ARQUIVO = "Lancamento.json"

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
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao
    }

    lancamentos.append(registro)
    salvar_lancamentos(lancamentos)

    print("Registro salvo com sucesso!")

# Exemplo de uso
if __name__ == "__main__":
    registrar()
