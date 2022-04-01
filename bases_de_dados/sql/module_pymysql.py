""""
pip install pymysql
base de dados from MySQL Workbench and Udemy
CRUD: Create Read Update Delete
"""

import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conecta():  # coloca gerenciador de contexto para nao ter que fechar a conexao sempre
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        print('conexao fechada')
        conexao.close()


#  CONEXAO 1 - Fazer as coisas
# adiciona um cliente
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome,idade,peso) VALUES' \
              '(%s,%s,%s,%s)'
        cursor.execute(sql, ('Jack', 'Bass', 72, 156))
        conexao.commit()
'''

# inserir dados de outra maneira
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'INSERT INTO clientes (nome, sobrenome,idade,peso) VALUES' \
              '(%s,%s,%s,%s)'
        dados = [
            ('Muriel', 'Figueireido', 19, 75),
            ('ROSE', 'Figueireido', 22, 55),
            ('JOSE', 'Figueireido', 21, 82),

        ]

        cursor.executemany(sql, dados)
        conexao.commit()
'''

# excluir  registro - uma id só
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id=%s'
        cursor.execute(sql, (6,))
        conexao.commit()
'''
# varias id de uma vez
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id IN (%s,%s,%s)'
        cursor.execute(sql, (7, 8, 9))
        conexao.commit()
'''
# usando BETWEEN
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'  # pode usar BETWEEN tb
        cursor.execute(sql, (7, 11))
        conexao.commit()
'''

# atualizar  registro
'''
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Martino', 5))
        conexao.commit()
'''

# CONEXAO 2 - Mostrar o que foi feito
with conecta() as conexao:
    with conexao.cursor() as cursor:  # gerador de contexto, nao precisa mais do open/close cursor
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')  # ordenar por ID decrescente (DESC =! ASC)
        # cursor.execute('SELECT nome, sobrenome FROM clientes')  # posso selecionar apenas o q precisa
        resultado = cursor.fetchall()
        for linha in resultado:
            # print(linha['nome'], linha['sobrenome']) # posso usar ferramenta de dict
            print(linha)
