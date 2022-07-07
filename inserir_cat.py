import sqlite3
conexao = sqlite3.connect('db2.sqlite3')
cursor = conexao.cursor()
categoria = input('Digite a categoria: ')
sql = '''
    INSERT into categoria(nome) values (?);
'''
valores = [categoria]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()