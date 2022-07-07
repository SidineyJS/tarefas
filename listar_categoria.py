import sqlite3
conexao = sqlite3.connect('db2.sqlite3')
cursor = conexao.cursor()

sql1 = '''
select * from categoria
'''
consulta = cursor.execute(sql1)
print('ID |  CATEGORIAS')
for categoria in consulta:
    print(categoria[0], categoria[1])