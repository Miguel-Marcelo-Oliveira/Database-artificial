# Base de Dados Artificial — Supermercado Fictício

---

## Sobre o Projeto

Script Python que **gera automaticamente uma base de dados sintética** de clientes de um supermercado fictício, contendo **120 registros** e **15 colunas** com informações realistas e coerentes entre si. Ao final, os dados são exportados para uma planilha **Excel (.xlsx)** pronta para análise.

O projeto foi desenvolvido como exercício prático de criação e manipulação de bases de dados com Python, aplicando boas práticas de consistência de dados — como garantir que o gênero sempre corresponda ao nome gerado, e que as cidades sempre correspondam ao estado selecionado.

---

## Funcionalidades

- Geração de 120 linhas de dados de clientes sintéticos
- Dados **consistentes e coerentes** entre colunas relacionadas (ex.: gênero × nome, cidade × estado)
- Distribuição aleatória controlada com `numpy.random`
- Exportação automática para planilha Excel com `pandas`
- Exibição formatada da tabela no terminal

---

## Estrutura da Base de Dados

| Coluna | Tipo | Descrição |
|---|---|---|
| `ID` | int | Identificador único do cliente |
| `Nomes` | str | Nome do cliente (lista pré-definida) |
| `Idade` | int | Idade entre 18 e 70 anos |
| `Salário (R$)` | float | Salário entre R$ 1.600 e R$ 35.000 |
| `Estado` | str | Sigla do estado (SP, RJ, MG, PR, BA, RS) |
| `Cidade` | str | Capital correspondente ao estado |
| `Escolaridade` | str | Nível de escolaridade |
| `Gênero` | str | Homem / Mulher — derivado do nome |
| `Compras` | int | Número de compras realizadas |
| `Primeira Compra` | date | Data da primeira compra (a partir de 02/02/2016) |
| `Última Compra` | date | Data da última compra (a partir de 12/04/2025) |
| `Cliente ativo` | str | Sim / Não |
| `Avaliação` | int | Nota de 1 a 10 |
| `Pagamento mais usado` | str | PIX / Débito / Crédito |
| `Categoria favorita` | str | Eletrônicos, Moda, Alimentos, Casa, Livros, Esportes, Estudos |

---

## Como Executar

### Pré-requisitos

- Python 3.x instalado
- Bibliotecas `pandas`, `numpy` e `openpyxl`

### Instalação das dependências

```bash
pip install pandas numpy openpyxl
```

### Execução

```bash
python base_de_dados_artificial.py
```

Após a execução, a tabela será exibida no terminal e o arquivo `base_de_dados_artificial.xlsx` será criado automaticamente no mesmo diretório.

---

## Conceitos Aplicados

- **Geração de dados sintéticos** com `numpy.random`
- **Criação e manipulação de DataFrames** com `pandas`
- **Consistência de dados relacionados** via lógica condicional (ex.: `nome → gênero`)
- **Mapeamento de dicionários** para relacionar estados e cidades
- **Exportação para Excel** com `DataFrame.to_excel()`
- **Formatação de datas** com `pd.date_range()`

---

## Tecnologias Utilizadas

| Biblioteca | Finalidade |
|---|---|
| `pandas` | Criação e exportação do DataFrame |
| `numpy` | Geração de valores aleatórios e arrays |
| `openpyxl` | Engine para escrita do arquivo `.xlsx` |

---

## Estrutura do Repositório

```
Database-artificial/
│
├── base_de_dados_artificial.py   # Script principal de geração dos dados
├── base_de_dados_artificial.xlsx # Planilha gerada (após execução)
└── README.md
```

---

## Autor

**Miguel Marcelo Alves Ramos de Oliveira**  
Estudante de Ciência da Computação — FIAP (2025–2029)  
[![GitHub](https://img.shields.io/badge/GitHub-Miguel--Marcelo--Oliveira-181717?style=flat&logo=github)](https://github.com/Miguel-Marcelo-Oliveira)

---

Feito com Python e curiosidade por dados
