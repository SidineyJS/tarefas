import sqlite3
conexao = sqlite3.connect('db.sqlite3')
sql = '''ALTER TABLE cliente ADD cpf TEXT;

'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()
