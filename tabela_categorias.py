import sqlite3
conexao = sqlite3.connect('db2.sqlite3')

sql = '''
    CREATE TABLE categoria (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT
);
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()
