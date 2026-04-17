import pandas as pd
import numpy as np

n_linhas = 120

estados_cidades = {
      "SP": "São Paulo",
      "RJ": "Rio de Janeiro",
      "MG": "Belo Horizonte",
      "PR": "Curitiba",
      "BA": "Salvador",
      "RS": "Porto Alegre"
}

# Criando uma lista apenas com os estados, que são as chaves do dicionário
estados = list(estados_cidades.keys())
col_estados = np.random.choice(estados, n_linhas)

# Criando listas de nomes masculinos e femininos
# Para depois relacionar com a colhna de gênero no DataFrame
# Evitando que haja confusão de dados e valores incoerentes
nomes_homem = ['Marcelo', 'Alexandre', 'Murilo', 'Ronaldo', 'Hugo', 'Pedro', 'Júlio', 'Antônio', 'Gabriel', 'Thiago']
nomes_mulher = ['Ana Luíza', 'Ingrid', 'Nathalia', 'Nátaly', 'Mariana', 'Sofia', 'Sarah', 'Giulia', 'Lara', 'Giovanna']

nomes_total = nomes_homem + nomes_mulher
nomes_escolhidos = np.random.choice(nomes_total, n_linhas)

# Criando um DataFrame
df = {"ID": range(1, n_linhas + 1),
      "Nomes": nomes_escolhidos,
      "Idade": np.random.randint(18, 70, n_linhas),
      "Salário (R$)": np.random.uniform(1600, 35000, n_linhas).round(2),
      "Estado": col_estados,
      "Cidade": [estados_cidades[estado] for estado in col_estados],
      "Escolaridade": np.random.choice(['Ensino Médio', 'Ensino Superior', 'Pós-Graduação', 'Mestrado', 'Doutorado'], n_linhas),
      "Gênero": ['Homem' if nome in nomes_homem else 'Mulher' for nome in nomes_escolhidos],
      "Compras": np.random.randint(1, 200, n_linhas),
      "Primeira Compra": pd.date_range(start="2016-02-02", periods=n_linhas, freq="D"),
      "Última Compra": pd.date_range(start="2025-04-12", periods=n_linhas, freq="D"),
      "Cliente ativo": np.random.choice(['Sim', 'Não'], n_linhas),
      "Avaliação": np.random.randint(1, 11, n_linhas),
      "Pagamento mais usado": np.random.choice(['PIX', 'Débito', 'Crédito'], n_linhas),
      "Nº de compras": np.random.randint(1, 200, n_linhas),
      "Categoria favorita": np.random.choice(['Eletrônicos', 'Moda', 'Alimentos', 'Casa', 'Livros', 'Esportes', 'Estudos'], n_linhas)
      }

df = pd.DataFrame(df)

# Exibindo a tabela de dados, sem a coluna que é gerada automaticamente
print(df.to_string(index=False))

# Importando a tabela criada artificialmente no formato Excel
df.to_excel('base_de_dados_artificial.xlsx', index=False)