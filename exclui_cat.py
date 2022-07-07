import sqlite3
conexao = sqlite3.connect('db2.sqlite3')
cursor = conexao.cursor()

id_excluir = input('Digite a id da categoria a ser deletada: ')
sql = '''
DELETE from categoria WHERE id=?
''' 
valores = [id_excluir]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()