"""
Projeto agenda com nome telefone

"""

import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?,?)'  # ignora se erro
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome =?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))  # % = qlqr coisa do lado da porcentagem

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Martin', '0601058289')
    # agenda.inserir('Martinho', '0601058289')  # nao vai entrar na base de dados pq telefone é unico
    # agenda.inserir('Rose', '0105025987')
    # agenda.inserir('Roberta', '0105325987')
    # agenda.inserir('Vinicius', '0105085987')
    # agenda.excluir(6)
    # agenda.inserir('Luiz Otávio', '1256589884')
    # agenda.inserir('Luiza Otávio', '1256589474')
    # agenda.inserir('Roger Luizinho Otávio', '1256489874')
    # agenda.inserir('Luizão', '1256589774')
    # agenda.inserir('Maria Luiza', '1212589874')

    agenda.buscar('luiz')

    # agenda.listar()
