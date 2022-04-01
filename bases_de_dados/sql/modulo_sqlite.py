"""
Aqui: tudo em Python, geralmente, trabalha na base de dados com programa externo

"""
import sqlite3

conexao = sqlite3.connect('basededados.db')  # objeto de conexao
cursor = conexao.cursor()  # objeto de cursor
#  base de dados vazia criada

cursor.execute('CREATE TABLE IF NOT EXISTS clientes('  # criação da tabela
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # criação da coluna id com preench auto
               'nome TEXT,'
               'peso REAL'  # Real = float
               ')')

# # INSERIR
# cursor.execute('INSERT INTO clientes(nome, peso) VALUES (?, ?)', ('Maria', 50))  # mandando um registro
# cursor.execute(
#     'INSERT INTO clientes(nome, peso) VALUES (:nome, :peso)',  # autra maneira
#     {'nome': 'Joazinho', 'peso': 25}
# )
# cursor.execute(
#     'INSERT INTO clientes VALUES (:id, :nome, :peso)',
#     {'id': None, 'nome': 'Daniela', 'peso': 113}
# )
# conexao.commit()  # executa o comando na base de dados (conexao)

# Atualizar
cursor.execute(
    'UPDATE  clientes SET nome=:nome, peso=:peso WHERE id=:id',
    {'nome': 'Joana','peso': 62, 'id': 2}
)

# EXCLUIR
cursor.execute(
    'DELETE FROM  clientes WHERE id=:id',  # CUIDADO COM ISSO: IRREVERSIVEL
    {'id': 5}
)
conexao.commit()
cursor.execute(
    'SELECT nome,peso FROM clientes WHERE peso > :peso',
    {'peso': 48}
               )  # busco todos os registros da tabela clientes

for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()
