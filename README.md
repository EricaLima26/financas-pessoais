# App de Finanças Pessoais

O App de Finanças Pessoais é um programa simples para registrar receitas e despesas, organizar extratos e gerar relatórios financeiros. Ele permite acompanhar o saldo total, visualizar lançamentos por categoria e exportar relatórios em arquivo de texto para análise posterior.

## Como rodar

```bash
python Financas.py
```

## Funcionalidades

1 - Registrar: Adiciona um novo lançamento (receita ou despesa) com valor, categoria e descrição.

2 - Ver extratos: Lista todos os lançamentos com data, tipo, categoria e valor formatado.

3 - Relatório: Exibe saldo total, total de receitas, total de despesas e totais por categoria.

4 - Exportar: Gera um arquivo relatorio.txt com o conteúdo do relatório.

5 - Sair: Encerra o programa.

## Funções implementadas

| Função | Responsabilidade |
|--------|-----------------|
| carregar() | Lê os lançamentos salvos no arquivo Lancamento.json. |
| salvar() | Grava os lançamentos atualizados no arquivo Lancamento.json. |
| registrar() | Solicita dados do usuário, valida entradas e adiciona um novo lançamento. |
| extrato() | Lista todos os lançamentos com data, tipo, categoria e valor formatado. |
| saldo() | Soma receitas e despesas para calcular o saldo total. |
| relatorio() | Monta o relatório com totais de receitas, despesas, saldo e categorias. |
| exportar() | Cria o arquivo relatorio.txt com o conteúdo do relatório. |

## Tecnologias usadas

Python 3

json

os

collections

## O que aprendi

Durante o desenvolvimento deste projeto, percebi a importância de estruturar o código em funções bem definidas para manter clareza e evitar repetições. A manipulação de arquivos JSON foi um ponto desafiador no início, mas me ajudou a entender melhor como persistir dados de forma simples e eficiente. Também ficou mais evidente como o tratamento de erros com `try/except` torna o programa mais robusto e amigável para o usuário. Além disso, aprendi a organizar o projeto em módulos separados (`opcao.py`, `financas.py`), o que facilita a manutenção e futuras expansões. Se começasse novamente, eu planejava desde o início a arquitetura do sistema, pensando em escalabilidade e na possibilidade de adicionar novas funcionalidades como exportação em CSV ou integração com banco de dados.
